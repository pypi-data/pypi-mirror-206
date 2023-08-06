import simpy
import requests
import math
from .utilities import get_current_tou, f_bus, get_buffer

"""## Classes
This program runs based on interaction of a few classes:

* The EV class defines bus objects.
* The Depot contains charging resources.
* The dispatcher function dispatches schedule blocks to the buses.

### Ebus

Each one has a bus_type (defaults to std), a generation (defaults to gen_1), and a battery capacity defaults to 500.
"""

class Ebus:
    def __init__(self, env, bussim, name, bus_type = 'std', gen = 'gen_1', capacity = 500):
        self.env = env
        self.name = name
        self.bussim = bussim
        self.depot = self.bussim.depot
        self.bus_tracker = self.bussim.bus_tracker
        self.gen = gen  # bus generation used for calculating energy consumption_kwh
        valid_gen = {'gen_1', 'gen_2', 'gen_3'}
        if self.gen not in valid_gen:
            raise ValueError(f'Bus gen must be in {valid_gen}')
        self.bus_type = bus_type
        valid_bus_type = {'std', 'art', 'exp'}
        if self.bus_type not in valid_bus_type:
            raise ValueError(f'Bus type must be in {valid_bus_type}')

        self.current_activity = 'parking'
        self.current_block = 'none'
        self.put_in_depot_proc = env.process(self.put_in_depot(env))

        self.bus_batt = simpy.Container(env, init=capacity, capacity=capacity) # create bus battery
        self.report_proc = env.process(self.report_status(env))
        self.charging_proc = env.process(self.charging(env))
        self.activity_tracker = [{'bus': self.name, 'start_time': 0, 'end_time': 0, \
                                  'current_activity': self.current_activity, 'current_block': self.current_block, \
                                  'current_soc': self.bus_batt.level / self.bus_batt.capacity}]

        self.charge = env.event()

    def put_in_depot(self, env):
        yield self.depot.depot_store.put(self) # put the bus in the store when it's created

    def drive(self, env, block):
        block_duration = block['end_time'] - block['dispatch_start_time']
        consumption_duration = block['consumption duration']
        avg_speed = block['consumption speed']
        mileage = block['consumption miles']
      
        # set bus current activity to begin driving
        self.current_activity = 'on_block' #f"{block['block_id']}_{block['start_time']}-{block['end_time']}"
        self.current_block = block['block']
        current_time = int(env.now)

        #while the bus is driving, subtract energy use every minute
        failed = 0
        while env.now < current_time + block_duration:
            
            yield env.timeout(1)

            if env.now < block['consumption_start_time']: continue # don't use energy until consumption time starts.

            kwh_consumption = self.calc_energy_use(avg_speed, mileage, consumption_duration, self.bussim.current_temp)
            
            if self.bus_batt.level < kwh_consumption: # Raise error if bus runs out of energy.
                share_completed = (env.now - block['dispatch_start_time']) / block_duration
                if not failed:
                    failure_record = {'bus':self.name, 'block':block['block'], 'time':env.now, 'share_completed':share_completed, \
                        'dispatch_start_time': block['dispatch_start_time'], 'end_time': block['end_time'], 'block_duration':block_duration}
                    self.bussim.block_failures.append(failure_record)
                failed = 1
                
            else:
                yield self.bus_batt.get(kwh_consumption)
            

        self.current_block = 'none'

        shift_time = get_buffer(env.now)
        self.current_activity = 'shifting'
        yield env.timeout(shift_time)

        yield self.depot.depot_store.put(self) # put bus back in depot.

        # Request use of resource
        with self.depot.charger.request() as req:
            # breakpoint()
            self.cancel_charge = env.event() # event in case bus is called to a block while waiting.
            req.bus = self
            req.name = self.name
            self.current_activity = 'waiting_to_charge'

            # Either successfully request charger and start charging, 
            # or cancel charge if bus goes to block instead.
            req_event = yield req | self.cancel_charge
            
            if not self.cancel_charge in req_event:
                self.charge = env.event()
                self.current_activity = 'charging'
                self.start_charge.succeed()
                
                # Once start_charge succeeds, the charging process starts, and continues until the charging process ends.

                yield self.charge # Finish charging and release charger
            
            else:
                self.bussim._cancel_events[self.cancel_charge.value].succeed()

    def charging(self, env):
        # bus charging behavior. each minute, either add charge, or cancel charging if the bus gets a cancel_charge command.
        while True:
            self.start_charge = env.event()
            yield self.start_charge
            
            while self.bus_batt.level < self.bus_batt.capacity:
                one_min = env.timeout(1)
                event = yield one_min | self.cancel_charge

                if self.cancel_charge not in event:
                    available_batt = self.bus_batt.capacity - self.bus_batt.level
                    actual_charge = min(self.depot.charging_speed, available_batt)
                    yield self.bus_batt.put(actual_charge)

                    # if charging isn't cancelled and the bus is full, then it starts parking
                    if self.bus_batt.level == self.bus_batt.capacity:
                        self.current_activity = 'parking'
                
                else:
                    self.bussim._cancel_events[self.cancel_charge.value].succeed()
                    break

            yield self.charge.succeed()

    def calc_energy_use(self, mph, mileage, block_duration, temp):
        
        miles_traveled_perminute = mileage / block_duration # miles traveled in the one minute btw calculations
        energy_used_permile = f_bus(self.gen, mph, temp, self.bus_type, perc=self.bussim.bus_percentile)
        energy_used_perminute = energy_used_permile * miles_traveled_perminute
        return energy_used_perminute        

    def report_status(self, env):
        while True:
            self.bus_tracker['time'].append(env.now)
            self.bus_tracker['bus'].append(self.name)
            self.bus_tracker['battery_pct'].append(self.bus_batt.level / self.bus_batt.capacity)
            self.bus_tracker['current_activity'].append(self.current_activity)
            self.bus_tracker['current_block'].append(self.current_block)

            if self.current_activity != self.activity_tracker[-1]['current_activity']:
                self.activity_tracker[-1]['end_time'] = env.now - 1
                self.activity_tracker.append({'bus': self.name, 'start_time': env.now, 'end_time': env.now, 'current_activity': self.current_activity, \
                                              'current_block': self.current_block, 'current_soc': self.bus_batt.level / self.bus_batt.capacity})
            if env.now == self.bussim.runtime-1:
                self.activity_tracker[-1]['end_time'] = env.now

            yield env.timeout(1)

"""### Depot

The depot is where power supply, number of chargers, and charger power are all set. The depot determines charging speed and requests power from the attached battery.
"""

class Depot:
    def __init__(self, env, bussim, chargers, charger_power, depot_power_supply, constrain_charging_power=False, battery=None, solar=None):
        self.env = bussim.env
        self.bussim = bussim
        self.tou_power_constraints = bussim.tou_power_constraints
        self.charge_speed_tracker = bussim.charge_speed_tracker
        self.chargers = chargers
        self.charger_power = charger_power / 60 # convert kw to "kwh per minute"
        self.depot_power_supply = depot_power_supply /60 # ditto
        self.constrain_charging_power = constrain_charging_power
        self.power_constraint = self.depot_power_supply # this will change based on tou constraints
        self.battery = battery
        if self.battery is not None:
            self.battery.home_depot = self # tell the battery where it is located
        self.solar = solar
        if self.solar is not None:
            self.solar.home_depot = self # tell the solar where it is located

        self.charger = simpy.Resource(env, capacity = self.chargers)
        self.electricity_usage = simpy.Container(env)
        self.depot_store = simpy.FilterStore(env) # Simpy "store" of charged buses that blocks request access to. Need to use a "FilterStore" so that different routes can request different types of buses.

        self.report_proc = env.process(self.report_status(env))
        self.charge_buses_proc = env.process(self.charge_buses(env))

        # charging speed that tells buses what speed to charge at
        # keep at 0.01 to prevent errors
        self.charging_speed = 0.01

        # events for passing information
        self.request_solar_discharge = env.event()
        self.request_battery_discharge = env.event()
        self.request_battery_charge = env.event()

        # trackers
        self.bus_tracker = {'buses_ready': [], 'buses_charging': [], 'buses_waiting_to_charge': [], 'blocks_waiting': []}
        self.power_tracker = {'available_power':[], 'allowed_power':[], 'grid_to_load': [], 'solar_to_load': [], 'solar_to_battery': [], 'solar_to_grid':[], 'battery_to_load': [], 'grid_to_battery':[], 'power_constraint':[]}
        self.electricity_usage_tracker = {'time': [], 'electricity_usage': []}
        self.charging_speed_tracker = []
        self.charger_tracker = []

    def charge_buses(self, env):
        while True:
            charger_users = self.charger.users.copy() # Copy to ensure a static list during each minute of bus charging.
            charger_count = len(charger_users)

            # set top charging speed: charger power times each connected bus, except for buses that are being topped off in the final minute of charging
            top_charging_speed = 0
            top_offs = {'buses': 0, 'charge': 0}
            for i in charger_users:
                bus = i.bus
                top_charge = min([self.charger_power, bus.bus_batt.capacity - bus.bus_batt.level])
                top_charging_speed += top_charge
                if top_charge < self.charger_power:
                    top_offs['buses'] += 1
                    top_offs['charge'] += top_charge

            # 1. charge buses with solar power (if available)
            if self.solar is not None:

                self.request_solar_discharge.succeed()
                self.request_solar_discharge = env.event()
                available_solar = yield self.solar.solar_response # get total available solar powerr
                solar_to_load = min([available_solar, max([0,top_charging_speed])])
                self.power_tracker['solar_to_load'].append(solar_to_load)

                # 1a. send any excess solar power to the battery
                excess_solar = available_solar - solar_to_load
                if excess_solar > 0 and self.battery is not None:
                    self.request_battery_charge.succeed(value = excess_solar)
                    self.request_battery_charge = env.event()
                    battery_charge_response = yield self.battery.battery_charge_response
                    self.power_tracker['solar_to_battery'].append(battery_charge_response)
                    excess_solar = excess_solar - battery_charge_response
                    if battery_charge_response:
                        self.battery.batt_container.put(battery_charge_response)
                else:
                    self.power_tracker['solar_to_battery'].append(0)

                # 1b. sell any remaining solar power to the grid
                if excess_solar:
                    self.power_tracker['solar_to_grid'].append(excess_solar)
                else:
                    self.power_tracker['solar_to_grid'].append(0)

            else:
                solar_to_load = 0
                self.power_tracker['solar_to_battery'].append(0)
                self.power_tracker['solar_to_load'].append(0)
                self.power_tracker['solar_to_grid'].append(0)

            # 2. charge buses with electric service
            # 2a. find grid power constraint
            if self.constrain_charging_power:
                current_tou = get_current_tou(self.bussim.start_date, env.now, self.bussim.tous)
                self.power_constraint = self.tou_power_constraints[current_tou] / 60
            else:
                self.power_constraint = float('inf')

            self.power_tracker['power_constraint'].append(self.power_constraint)
            allowed_power = min([self.depot_power_supply, self.power_constraint])
            self.power_tracker['allowed_power'].append(allowed_power)

            # grid to load is either the max allowed power based on supply and tou or top charging speed minus solar already applied, whichever is less.
            grid_to_load = min([top_charging_speed - solar_to_load, allowed_power])
            self.power_tracker['grid_to_load'].append(grid_to_load)

            # 3. charge buses with battery power (if needed and available)
            if top_charging_speed > grid_to_load + solar_to_load and self.battery is not None:
                self.request_battery_discharge.succeed(value = top_charging_speed - grid_to_load - solar_to_load) # request diff between top charging and allowed power - the battery will send the most that it can
                self.request_battery_discharge = env.event() #reset request event
                # wait for response from battery...
                battery_to_load = yield self.battery.battery_response
                if battery_to_load: # Need if statement to avoid requesting 0 charge
                    self.battery.batt_container.get(battery_to_load)
            else:
                battery_to_load = 0
            self.power_tracker['battery_to_load'].append(battery_to_load)

            # 4. set actual charging speed.
                # the charging speed is grid to load plus battery to load + solar to load 
                # divided by number of buses charging
            if charger_count > 0:
                # charging speed is available charge divided by number of buses.
                # if there are buses topping off, the bit of charge they need is subtracted from the numerator and the num of topoff buses subtracted from denominator
                # the buses themselves will request less than max charge if they can't handle it.
                charging_speed = ((grid_to_load + solar_to_load + battery_to_load) - top_offs['charge']) / max([(charger_count - top_offs['buses']),1])
                self.charging_speed = max([charging_speed, 0.01])
            else:
                charging_speed = 0
                self.charging_speed = 0.01

            # OLD CHARGING BEHAVIOR
            # 5. charge the buses
            # for i in charger_users:
            #     bus = i.bus
            #     if bus.charge.triggered:
            #         continue
                                
            #     max_charge = bus.bus_batt.capacity - bus.bus_batt.level
            #     actual_charge = min([charging_speed, max_charge])
                
            #     if actual_charge:
            #         yield bus.bus_batt.put(actual_charge)
            #         yield self.electricity_usage.put(actual_charge)
                
            #     self.charge_speed_tracker[bus.name][env.now-1] = actual_charge
                
            #     # when bus capacity is full, mark charging as complete
            #     if bus.bus_batt.level == bus.bus_batt.capacity:
            #         bus.charge.succeed()

            # 5. if there is leftover grid power use it to charge the battery
            available_power = max([allowed_power - top_charging_speed, 0])
            self.power_tracker['available_power'].append(available_power)
            if available_power > 0 and self.battery is not None:
                self.request_battery_charge.succeed(value = available_power)
                self.request_battery_charge = env.event()
                battery_charge_response = yield self.battery.battery_charge_response
                self.power_tracker['grid_to_battery'].append(battery_charge_response)
                if battery_charge_response:
                    self.battery.batt_container.put(battery_charge_response)
            else:
                self.power_tracker['grid_to_battery'].append(0)

            yield env.timeout(1)

                           

    def report_status(self, env):
        while True:
            self.bus_tracker['buses_ready'].append(len(self.depot_store.items))
            self.bus_tracker['buses_charging'].append(self.charger.count)
            self.bus_tracker['buses_waiting_to_charge'].append(len(self.charger.queue))
            self.bus_tracker['blocks_waiting'].append(len(self.depot_store.get_queue))

            self.electricity_usage_tracker['time'].append(env.now)
            self.electricity_usage_tracker['electricity_usage'].append(self.electricity_usage.level)
            self.charging_speed_tracker.append(self.charging_speed)
            self.charger_tracker.append(len(self.charger.users))

            yield env.timeout(1)

"""### Battery

The battery has energy and power. It provides as much energy as possible for charging buses, and also charges as rapidly as possible when not charging buses.
"""

class Battery:
    def __init__(self, env, energy, power):
        self.env = env
        self.energy = energy
        self.power = power / 60 # convert kw to kwh / minute
        self.home_depot = None # home_depot is set by the depot that owns the battery
        self.batt_container = simpy.Container(env, init=energy*0.5, capacity=energy)

        self.discharge_proc = env.process(self.set_discharge_speed(env))
        self.charge_proc = env.process(self.set_charge_speed(env))

        self.soc = self.batt_container.level / self.batt_container.capacity # battery state of charge
        self.soc_tracker = []
        self.tracker_proc = env.process(self.tracker(env))

        # battery response events
        self.battery_response = env.event()
        self.battery_charge_response = env.event()

    def set_discharge_speed(self, env):
        while True:
            requested_discharge = yield self.home_depot.request_battery_discharge
            available_discharge = min([self.power, self.batt_container.level, requested_discharge])
            self.battery_response.succeed(value = available_discharge)
            self.battery_response = env.event()

    def set_charge_speed(self, env):
        while True:
            requested_charge = yield self.home_depot.request_battery_charge
            available_charge = min([self.power, self.batt_container.capacity - self.batt_container.level, requested_charge])
            self.battery_charge_response.succeed(value = available_charge)
            self.battery_charge_response = env.event()

    def tracker(self, env):
        while True:
            self.soc = self.batt_container.level / self.batt_container.capacity
            self.soc_tracker.append(self.soc)
            yield env.timeout(1)

"""### Solar

Solar energy system class, which calculates solar energy generation using the NREL [PVWatts API](https://developer.nrel.gov/docs/solar/pvwatts/v6/).
"""

# Solar class gets solar energy production data using the PVWatts API.
# API info at https://developer.nrel.gov/docs/solar/pvwatts/v6/
class Solar:
    def __init__(self, env, bussim, depot, api_key='vgbbhTeXKmNmf050jwWrJD6UZmKbkVAGibOwRhAd', system_capacity=500, module_type=0, losses=14.08, array_type=0, tilt=20, azimuth=180):
        self.env = env
        self.bussim = bussim
        self.home_depot = None
        self.payload={
                'api_key': api_key,
                'system_capacity': system_capacity,
                'module_type': module_type,
                'losses': losses,
                'array_type': array_type,
                'tilt': tilt,
                'azimuth': azimuth,
                'address': self.bussim.depot_info.loc[depot]['address'],
                'timeframe': 'hourly'
        }
        self.url = r'https://developer.nrel.gov/api/pvwatts/v8.json?'
        # api info at https://developer.nrel.gov/docs/solar/pvwatts/v6/
        # new api info at https://developer.nrel.gov/docs/solar/pvwatts/v8/
        self.r = requests.get(self.url, params=self.payload)
        self.r_data = self.r.json()
        self.ac = [i/1000/60 for i in self.r_data['outputs']['ac']] # convert watt-minute to kwh
        self.dc = [i/1000/60 for i in self.r_data['outputs']['dc']]

        self.solar_output_proc = env.process(self.solar_output(env))
        self.solar_discharge_proc = env.process(self.solar_discharge(env))

        self.dc_output = 0
        self.dc_tracker = []

        self.solar_response = env.event()

    def solar_output(self, env):
        while True:
            start_hour = (self.bussim.start_date.day_of_year - 1) * 24
            current_hour = (start_hour + (math.ceil(env.now / 60) - 1)) % 8760 # modulus in case goes over 8760
            dc_solar_out = self.dc[current_hour]
            self.dc_output = dc_solar_out
            self.dc_tracker.append(self.dc_output)
            yield env.timeout(1)

    def solar_discharge(self, env):
        while True:
            requested_discharge = yield self.home_depot.request_solar_discharge
            self.solar_response.succeed(value = self.dc_output)
            self.solar_response = env.event()

"""### Dispatch

The dispatch function dispatches buses at their designated start time.
"""

def dispatch(env, bussim, block, block_waittime):

    block_tracker, depot, bus_gen, bus_batt_min, bus_kwh_capacity = bussim.block_tracker, bussim.depot, bussim.bus_gen, bussim.bus_batt_min, bussim.bus_kwh_capacity
    # the bus batt max is if you dont want to dispatch charging buses that are almost finished charging. set to below 1
    bus_batt_max = 1 * bus_kwh_capacity[bus_gen][block['type']]

    # wait for X minutes before block start time and then begin dispatch process!
    # wait time to account for shifting
    # in the first 15 minutes, can't call before 0, so just call as early as possible and wait that amount of time.
    
    # This is the shift time for the bus to leave the depot. There is a separate shift time for the bus to return to the depot.
    shift_time = 0 
    call_time = max([block['dispatch_start_time'] - shift_time, 0])  
    actual_shift_time = block['dispatch_start_time'] - call_time  # actual shift time corrects for first shifts of the day to prevent negative call times
    yield env.timeout(call_time)

    block_energy_need = f_bus(bus_gen, block['dispatch speed'], bussim.current_temp, block['type'], bussim.bus_percentile) * block['dispatch miles']

    # The following code either dispatches a bus, or cancels the dispatch request if too long passes without a bus available.
    # The get_bus function uses a lambda function to only take out buses that match the block vehicle type (std, art, or exp)

    def bus_pick(bus):
        return any([
            all([bus.bus_type == block['type'],
                 bus.current_activity == "parking",
                 bus.bus_batt.level == bus_kwh_capacity[bus_gen][block['type']]]),
            
            all([bus.bus_type == block['type'],
                any([bus.current_activity == "charging", bus.current_activity == "waiting_to_charge"]),
                bus.bus_batt.level > block_energy_need, 
                bus.bus_batt.level > bus_batt_min,
                bus.bus_batt.level < bus_batt_max])
            ])

    if block_energy_need > bus_kwh_capacity[bus_gen][block['type']]: # don't attempt to run bus if there are no buses with big enough battery
        block['status'] = 'dropped_energy'

    else:
        get_bus = depot.depot_store.get(lambda bus: bus_pick(bus))
        block_timeout = env.timeout(block_waittime, value='nobus')

        bus_dispatch = yield get_bus | block_timeout # Yield when either get_bus or block_timeout occurs. Simpy "AnyOf" event using the "or" operator
                    
        if get_bus in bus_dispatch: # If get_bus is one of the successful events, then proceed to dispatch it.
            bus = get_bus.value
            block_index = str(block['block_index'])
            

            if bus in [i.bus for i in bus.depot.charger.queue] or bus in [i.bus for i in bus.depot.charger.users]: # cancel charge if bus is queuing
                # ensure that the dispatch waits for the cancelled charge to yield
                bussim._cancel_events[block_index] = env.event()
                bus.cancel_charge.succeed(value = block_index)
                # do not yield/ dispatch the bus until the cancel_event succeeds. 
                # this is designed to ensure that the bus doesn't end up in two places at once.
                yield bussim._cancel_events[block_index]

            # move the bus out of the depot to start its block
            bus.current_activity = 'shifting'
            yield env.timeout(actual_shift_time) 

            env.process(bus.drive(env, block)) # send the bus off on its route
            block['status'] = 'run'

        else:
            block['status'] = 'dropped_no_bus'
            get_bus.cancel()

    block['actual_time'] = env.now
    for i in ['block', 'dispatch_start_time', 'actual_time', 'status']:
        block_tracker[i].append(block[i])
