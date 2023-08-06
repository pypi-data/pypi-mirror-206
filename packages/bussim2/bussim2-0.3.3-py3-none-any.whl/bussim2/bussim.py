# -*- coding: utf-8 -*-
import simpy
import json
import os
import shutil
import datetime
import math
import sqlite3
import configparser
from functools import partial
import requests
import time
import webbrowser
from airium import Airium
import pandas as pd
import matplotlib.pyplot as plt
from .bussimclasses import Ebus, Depot, Battery, Solar, dispatch
from .utilities import BlockData, calc_demand_costs, calc_energy_costs, list_sql_tables


package_dir = os.path.dirname(os.path.abspath(__file__))
blocks_file = os.path.join(package_dir, 'sources', 'blocks.db')

# BusSim class, each bus sim is an object with simulation outputs.
class BusSim:
    '''Run a bus simulation.
    '''

    def __init__ (self, *, depot_name, start_date, num_days, std_bus_num, art_bus_num, exp_bus_num, \
            charger_power, chargers, depot_power_supply, block_waittime, rate_type, constrain_charging_power, \
            bus_gen='gen_1', peak_constraint=0, shoulder_constraint=0, battery_kwh=0, battery_hours=4, solar_kw=0, \
            bus_batt_min = 100, real_temp = True, temp = 20, blocks_sqltable = "blocks_originals", run_until=None, \
            bus_percentile = False, superblocks = False, usable_battery = 1):
        
        self.meta_data = locals()
        self.depot_name = depot_name
        self.start_date = start_date
        self.num_days = num_days
        self.bus_nums = {'std': std_bus_num, 'art': art_bus_num, 'exp': exp_bus_num}
        # load battery size assumptions from csv
        self.bus_kwh_capacity = pd.read_csv(os.path.join(package_dir, 'sources', 'bus_battery_sizes.csv'), index_col=0) * usable_battery
        self.bus_kwh_capacity = self.bus_kwh_capacity.to_dict(orient='index')
        self.bus_batt_min = bus_batt_min
        self.charger_power = charger_power
        self.chargers = chargers
        self.depot_power_supply = depot_power_supply
        self.block_waittime = block_waittime
        self.rate_type = rate_type
        self.bus_gen = bus_gen
        self.constrain_charging_power = constrain_charging_power
        self.peak_constraint = peak_constraint
        self.shoulder_constraint = shoulder_constraint
        self.battery_kwh = battery_kwh
        self.battery_hours = battery_hours
        self.solar_kw = solar_kw
        self.real_temp = real_temp # whether or not sim uses NREL temps, or set a constant temp manually
        self.blocks_sqltable = blocks_sqltable
        self.bus_percentile = bus_percentile
        self.superblocks = superblocks

        # bussim timestamp for generating file outputs
        t = time.localtime()
        self.timestamp = time.strftime('%Y%m%d%H%M', t)
        self.output_folder = os.path.join(os.getcwd(), 'outputs', self.depot_name + self.timestamp)


        # load nypa power and energy rates
        self.energy_rates = pd.read_csv(os.path.join(package_dir, 'sources', 'energy_rates.csv'), index_col=[0,1]).sort_index()
        self.demand_rates = pd.read_csv(os.path.join(package_dir, 'sources', 'demand_rates.csv'), index_col=[0,1,2]).sort_index()

        # load depot info
        self.depot_info = pd.read_csv(os.path.join(package_dir, 'sources', 'depot_info.csv'), index_col=[0])

        # load temps and set initial temp to None
        if self.real_temp:        
            self.temps = self.get_temps()
            self.current_temp = None
        else:   # or use the manually set temperature
            self.current_temp = temp

        self.figsize = (10, 7) # figure size in inches

        # set tous
        self.tou_power_constraints = {'8a-06p_m-f': peak_constraint, '8a-10p_m-f': shoulder_constraint, 'all_else': float('inf')} # limits in kw; can't set limit to 0 or the sim breaks.
        self.tous = {'8a-06p_m-f': list(range(8,18)), '8a-10p_m-f': list(range(8, 22)), 'all_else': list(range(0,24))} # note that tou also depends on season.
        self.tou_days = {'peak_days': list(range(0,5)), 'offpeak_days': list(range(5, 7))}

        # Old code to load bus energy consumption rates.
        # Bus energy consumption is now governed by f_bus function in "utilities.py."
            # load energy consumption use rates
            # self.std_bus_energy_rates = pd.read_csv(os.path.join(package_dir, 'sources', 'std_bus_energy_rates.csv'), index_col=[0])
            # # self.bus_reg_terms = pd.read_csv(os.path.join(package_dir, 'sources', 'bus_reg_terms.csv'), index_col=[0]) # for energy regression
            # self.art_energy_rates = self.std_bus_energy_rates * 1.4
            # self.exp_energy_rates = self.std_bus_energy_rates * 1.15
            # self.bus_energy_rates = pd.concat([self.std_bus_energy_rates, self.art_energy_rates, self.exp_energy_rates], keys=['std', 'art', 'exp'])

        # load block data
        self._blocks_db = blocks_file

        # make blocks
        self._block_data = BlockData(self.depot_name, self.start_date, self._blocks_db, blocks_table = self.blocks_sqltable, days=self.num_days, superblocks = self.superblocks)
        self._full_blocks_dict = self._block_data.full_blocks
        self._full_blocks = self._block_data.full_blocks_df
        
        if not run_until:
            self.runtime = self._block_data.max_time
        else:
            self.runtime = run_until

        # set up bus names and trackers and data
        self.total_buses = sum(self.bus_nums.values())
        self.bus_zfill = 3

        self.std_buses = [f'std_{str(i).zfill(self.bus_zfill)}' for i in range(1, self.bus_nums['std'] + 1)]
        self.art_buses = [f'art_{str(i).zfill(self.bus_zfill)}' for i in range(1, self.bus_nums['art'] + 1)]
        self.exp_buses = [f'exp_{str(i).zfill(self.bus_zfill)}' for i in range(1, self.bus_nums['exp'] + 1)]

        self.bus_tracker = {'time': [], 'bus': [], 'battery_pct': [], 'current_activity': [], 'current_block':[]}
        self.block_tracker={'block':[], 'dispatch_start_time':[], 'actual_time':[], 'status':[]}

        self.block_failures = []
        self.power_limited_tracker = []
        self.charge_speed_tracker = {}
        for i in self.std_buses + self.art_buses + self.exp_buses:
            self.charge_speed_tracker[i] = [0 for t in range(self.runtime)]

        # init environment, processes, and then run
        self.env = simpy.Environment()

        # initiate process to set temperatures
        if self.real_temp:
            self.env.process(self.set_temp())

        if self.battery_kwh:
            self.battery = Battery(self.env, energy=self.battery_kwh, power=self.battery_kwh/self.battery_hours) # To remove battery, set battery = None
        else:
            self.battery = None

        if self.solar_kw:
            self.solar = Solar(self.env, self, self.depot_name, system_capacity=self.solar_kw)
        else:
            self.solar = None

        self.depot = Depot(self.env, self, chargers=self.chargers, \
                                             charger_power=self.charger_power, depot_power_supply=self.depot_power_supply, \
                                             constrain_charging_power=self.constrain_charging_power, battery=self.battery, solar=self.solar)  # charger_power and depot_power_supply units are kw

        # make bus objs / capacity units are kwh
        self.bus_objs = {'std': [Ebus(self.env, self, i, bus_type='std', capacity=self.bus_kwh_capacity[self.bus_gen]['std'], gen=self.bus_gen) for i in self.std_buses],
                         'art': [Ebus(self.env, self, i, bus_type='art', capacity=self.bus_kwh_capacity[self.bus_gen]['art'], gen=self.bus_gen) for i in self.art_buses],
                         'exp': [Ebus(self.env, self, i, bus_type='exp', capacity=self.bus_kwh_capacity[self.bus_gen]['exp'], gen=self.bus_gen) for i in self.exp_buses]}
               
        # run dispatch process
        self._cancel_events = {} # for yielding bus dispatch events
        [self.env.process(dispatch(self.env, self, block, self.block_waittime)) for block in self._full_blocks_dict]

        # Run simulation
        self.start_date = self._full_blocks['date'].min()
        self.date_range = pd.period_range(self._full_blocks['date'].min(), periods = self.runtime, freq='min')
        # print(f"Running analysis from {self.full_blocks['date'].min()} to {self.full_blocks['date'].max()}...", end=' ')
        
        self.env.run(until = self.runtime)
        # print(f'Done.')

        # CREATE DATA TRACKER OUTPUTS
        # create data for output and functions
        self._full_blocks['duration_hours'] = self._full_blocks['duration'] / 60
        self._full_blocks['mileage_1000s'] = self._full_blocks['consumption miles'] / 1000
        self.full_blocks_tracked = self._full_blocks.merge(pd.DataFrame(self.block_tracker), on=['block', 'dispatch_start_time'])

        # bus and block tracking
        self.data_tracker_df = pd.DataFrame(self.depot.bus_tracker).set_index(self.date_range, drop=True)
        self.data_tracker_df['buses_on_blocks'] = self.total_buses - self.data_tracker_df['buses_ready'] - self.data_tracker_df['buses_charging'] - self.data_tracker_df['buses_waiting_to_charge']

        # depot power tracking
        self.depot_power_tracker_df = pd.DataFrame(self.depot.power_tracker).set_index(self.date_range, drop=True)
        self.depot_power_tracker_df['total_to_load'] = self.depot_power_tracker_df['battery_to_load'] + self.depot_power_tracker_df['grid_to_load'] + self.depot_power_tracker_df['solar_to_load']
        self.depot_power_tracker_df['total_to_battery'] = self.depot_power_tracker_df['solar_to_battery'] + self.depot_power_tracker_df['grid_to_battery']

        # total power tracking
        self.charge_speed_tracker_df = pd.DataFrame(self.charge_speed_tracker)
        self.charge_speed_tracker_df.set_index(self.date_range, drop=True, inplace=True)
        self.minutely_energy_consumption = self.charge_speed_tracker_df.sum(axis=1)
        self.minutely_energy_consumption_kw = self.minutely_energy_consumption * 60 # times 60 to convert from kwh per minute to kw

        # bus tracking
        # battery pct
        self._bus_battery_df = pd.DataFrame(self.bus_tracker).pivot(index='time', columns='bus', values='battery_pct').set_index(self.date_range, drop=True)
        self.bus_tracker_df = pd.DataFrame(self.bus_tracker)
        # activities
        self.bus_pivot = self.bus_tracker_df.pivot_table(values='bus', columns='current_activity', index='time', aggfunc='count', fill_value=0)
        self.bus_pivot.set_index(self.date_range, drop=True, inplace=True)

        # depot battery tracking
        if self.battery: self.soc_tracker_series = pd.Series(data = self.battery.soc_tracker, index = self.date_range)

        # ELECTRICITY COSTS
        # energy
        self.total_grid_demand = self.depot_power_tracker_df['grid_to_load'] + self.depot_power_tracker_df['grid_to_battery']
        self.hourly_energy_consumption = calc_energy_costs(self.total_grid_demand, self.energy_rates)
        self.monthly_energy_consumption = self.hourly_energy_consumption['consumption_kwh'].resample('m').sum()
        self.monthly_energy_costs = (self.hourly_energy_consumption['energy_cost']).resample('m').sum()

        #demand
        self.peak_demand_df = calc_demand_costs(self.total_grid_demand, self.demand_rates, self.tou_days, self.tous, self.rate_type)
        # group demand charge by month and tou and get max
        self.demand_charge_df = self.peak_demand_df.groupby(['month', 'tou']).max()
        # and then sum up each demand charge by month
        self.monthly_demand_charge = self.demand_charge_df.groupby('month')['demand_charge'].sum()

        # solar exports
        self.dollars_per_kwh = 0.17 # compensation for exported electricity
        self.solar_export_rev = self.depot_power_tracker_df['solar_to_grid'].resample('M').sum() * self.dollars_per_kwh
        self.solar_export_rev.name = ('solar_export_rev')

        # total costs
        self.total_costs = pd.concat([self.monthly_demand_charge, self.monthly_energy_costs, -self.solar_export_rev], axis=1)
        self.total_costs_table = self.total_costs.copy()
        self.total_costs_table['total'] = self.total_costs_table.sum(axis=1)
        self.total_costs_table = self.total_costs_table.style.format("${:,.2f}")

        # BLOCK INFO
        self.blocks_run = self.blocks_table().at['run', 'num_blocks']
        self.blocks_run_per_bus = self.blocks_run / sum(self.bus_nums.values())
        self.miles_run = self.blocks_table().at['run', 'miles_1000s']
        self.hours_run = self.blocks_table().at['run', 'duration_hours']
        self.blocks_total = self.blocks_table()['num_blocks'].sum()
        self.miles_total = self.blocks_table()['miles_1000s'].sum()
        self.hours_total = self.blocks_table()['duration_hours'].sum()

        self.blocks_by_bustype = self.full_blocks_tracked.groupby(['type', 'status'])['status'].count()
        self.blocks_by_bustype.name = "block count"
        self._bus_nums_s = pd.Series(self.bus_nums)
        self.blocks_per_bustype = self.blocks_by_bustype.div(self._bus_nums_s, axis='index', level=0)

        if self.block_failures:
            print(f'Warning: {len(self.block_failures)} block(s) failed during bus simulation.')

    def get_temps(self):
        '''load annual hourly temperature from NREL.'''
        url = r'https://developer.nrel.gov/api/pvwatts/v8.json?'
        payload={
            'api_key': 'vgbbhTeXKmNmf050jwWrJD6UZmKbkVAGibOwRhAd',
            'system_capacity': 100,
            'module_type': 0,
            'losses': 14.08,
            'array_type': 0,
            'tilt': 20,
            'azimuth': 180,
            'address': self.depot_info.loc[self.depot_name]['address'],
            'timeframe': 'hourly'}
        # try to load temps from NREL - if not, just use default temps, which are from Kingsbridge location for 2022.
        try:
            r = requests.get(url, params=payload)
            c_temps = r.json()['outputs']['tamb']
        except:
            # nyc_temps was the json response for kingsbridge
            print('Warning: No access to external API. Using default NYC temperature file.')
            with open(os.path.join(package_dir, 'sources', 'nyc_temps.json')) as file:
                j = file.read()
            c_temps = json.loads(j)['outputs']['tamb']
        f_temps = [i * 9/5 + 32 for i in c_temps]
        return f_temps

    def set_temp(self):
        '''Set temperature every hour.'''
        start_hour = (self.start_date.day_of_year - 1) * 24
        while True:
            current_hour = (start_hour + (math.ceil(self.env.now / 60) - 1)) % 8760 # modulus in case goes over 8760
            self.current_temp = self.temps[current_hour] # set temperature for the sim
            yield self.env.timeout(60) #update temperature every 60 minutes

    def blocks_plot(self, chart_days=0, out=False):
        # choose how many days to display in charts
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        block_times = self.full_blocks_tracked[['dispatch_start_time', 'end_time']].to_dict(orient='records')
        possible_block_times = self.full_blocks_tracked[self.full_blocks_tracked['status'] != 'dropped_energy'][['dispatch_start_time', 'end_time']].to_dict(orient='records')
        run_block_times = self.full_blocks_tracked[self.full_blocks_tracked['status'] == 'run'][['dispatch_start_time', 'end_time']].to_dict(orient='records')
        block_count = []
        possible_block_count = []
        run_block_count = []

        def get_times(t, times_df):
            filt_times = filter(lambda x: all([x['start_time'] <= t, x['end_time'] >= t]), times_df)
            return len(list(filt_times))

        for t in range(self.runtime):
            block_count.append(get_times(t, block_times))
            possible_block_count.append(get_times(t, possible_block_times))
            run_block_count.append(get_times(t, run_block_times))

        block_count_df = pd.DataFrame(index=self.date_range, data={'block_count':block_count, 'possible_block_count':possible_block_count, 'run_block_count':run_block_count})
        blocksplot = block_count_df.loc[self.start_date:end_chart_date].plot(ylabel='blocks', figsize=self.figsize)

        if out:
            blocksplot.figure.savefig(os.path.join(self.output_folder, "blocksplot"))

    def blocks_table(self):
        # Info about blocks that were run or were dropped
        block_group = self.full_blocks_tracked.groupby('status')
        return block_group.agg(
                num_blocks = ('block', len),
                miles_1000s = ('mileage_1000s', sum),
                duration_hours = ('duration_hours', sum),
        )

    def blocks_bustype_table(self):
        # Info about blocks that were run or were dropped
        block_group = self.full_blocks_tracked.groupby(['type', 'status'])
        return block_group.agg(
                num_blocks = ('block', len),
                miles_1000s = ('mileage_1000s', sum),
                duration_hours = ('duration_hours', sum),
        )

    def blocks_daily_table(self):
        run_blocks = self.full_blocks_tracked[self.full_blocks_tracked['status'] == 'run'].copy()
        block_day_group = run_blocks.groupby(['day', 'day_type'])
        return block_day_group.agg(
                num_blocks = ('block', len),
                miles_1000s = ('mileage_1000s', sum),
                duration_hours = ('duration_hours', sum),
        )

    def blocks_gantt_plot(self, chart_days=0):
        if chart_days: chart_days = min([self._full_blocks['date'].nunique(), chart_days])
        else: chart_days = self._full_blocks['date'].nunique()

        block_days = self._full_blocks[self._full_blocks['date'].isin(self._full_blocks['date'].unique()[0:chart_days])]

        max_time = block_days['end_time'].max() + 1
        for i in block_days.iterrows():
            plt.hlines(i[0], i[1]['start_time'], i[1]['end_time'], 'red' if i[1]['type'] == 'art' else 'blue' if i[1]['vehicle_type'] == 'exp' else 'black')

    def activity_tracker_df(self, buses=None, df=True):
        all_bus_objs = self.bus_objs['std'] + self.bus_objs['art'] + self.bus_objs['exp']
        if buses:
            all_bus_objs = all_bus_objs[0:buses]
        activity_tracker = []
        bus_names = []
        for i in all_bus_objs:
            activity_tracker += i.activity_tracker
            bus_names.append(i.name)
        if df:
            return pd.DataFrame(activity_tracker)
        else:
            return activity_tracker
        
    
    def bus_activity_gantt(self, buses=None, out=False):
        activity_colors = {'parking': 'green', 'waiting_to_charge': 'orange', 'charging': 'blue', 'on_block': 'red', 'shifting': 'yellow'}
        
        # set max number of buses to chart at 10
        num_buses = min([sum(self.bus_nums.values()), 10])

        num_bus_types = bool(self.std_buses) + bool(self.art_buses) + bool(self.exp_buses)
        num_per_type = max([1,int(num_buses / num_bus_types)])

        # chart of battery percentage for buses
        std_bus_chart = self.bus_objs['std'][0:min(num_per_type, self.bus_nums['std'])]
        art_bus_chart = self.bus_objs['art'][0:min(num_per_type, self.bus_nums['art'])]
        exp_bus_chart = self.bus_objs['exp'][0:min(num_per_type, self.bus_nums['exp'])]
        
        all_bus_objs = std_bus_chart + art_bus_chart + exp_bus_chart

        num_buses = min([len(all_bus_objs), 10])

        activity_tracker = []
        bus_names = []
        for i in all_bus_objs:
            activity_tracker += i.activity_tracker
            bus_names.append(i.name)
        fig, ax = plt.subplots(figsize=(10,7))
        ax.set_yticks(range(len(bus_names)))
        ax.set_yticklabels(bus_names)
        # ax.set_xticks(len(self.date_range))
        # ax.set_xticklabels(self.date_range, rotation=45)

        linewidths = 170/(len(bus_names)+1)
        for i in activity_tracker:
            ax.hlines(bus_names.index(i['bus']), i['start_time'], i['end_time'], activity_colors[i['current_activity']], linewidths=linewidths, label=i['current_activity'])
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))  
        plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.1, 1.05))

        if out:
            plt.savefig(os.path.join(out,'gantt'))

    def bus_plot(self, chart_days=0, out=False):
        '''Plot of bus activity throughout simulation.'''

        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()
        busplot_df = self.bus_pivot.loc[self.start_date:end_chart_date]
        busplot = busplot_df.plot(ylabel='buses', figsize=self.figsize)

        # self.data_tracker_df.loc[self.start_date:end_chart_date].plot(ylabel='buses/blocks', figsize=self.figsize)
        if out:
            busplot.figure.savefig(os.path.join(out,'busplot'))
            busplot_df.to_csv(os.path.join(out,'busplot.csv'))


    def power_plot(self, chart_days=0, out=False):
        '''Create plot of power use over time. If want to output a file, set 'out' equal to a directory name.'''
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()
        max_strings = [
            f"Charging constrained during peak hours: {self.constrain_charging_power}",
            f"Max total to load: {self.depot_power_tracker_df['total_to_load'].max() * 60:,} kw",
            f"Max solar to load: {self.depot_power_tracker_df['solar_to_load'].max() * 60:,} kw",
            f"Max battery to load: {self.depot_power_tracker_df['battery_to_load'].max() * 60:,} kw",
            f"Max grid to load: {self.depot_power_tracker_df['grid_to_load'].max() * 60:,} kw",
        ]

        if not out:
            for i in max_strings:
                print(i)
        
        powerdf = (self.depot_power_tracker_df[['total_to_load', 'grid_to_load', 'grid_to_battery', 'battery_to_load', 'solar_to_load', 'solar_to_battery']] * 60).loc[self.start_date:end_chart_date]
        powerplot = powerdf.plot(ylabel='kw', figsize=self.figsize)

        if out:
            powerplot.figure.savefig(os.path.join(out, "powerplot"))
            powerdf.to_csv(os.path.join(out, 'powerplot.csv'))
            return max_strings

    def total_power_plot(self, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        print(f'Max minute demand is {(self.minutely_energy_consumption_kw).max()} KW')
        self.minutely_energy_consumption_kw[self.start_date:end_chart_date].plot(ylabel='KW', figsize=self.figsize)

    def grid_demand_plot(self, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        (self.total_grid_demand[self.start_date:end_chart_date] * 60).plot(ylabel='KW', figsize=self.figsize)

    def solar_plot(self, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()
        (self.depot_power_tracker_df[['solar_to_battery', 'solar_to_grid', 'solar_to_load']] * 60).loc[self.start_date:end_chart_date].plot(ylabel='kw', figsize=self.figsize, kind='area')

        #if self.solar:
        #  solar_series = pd.Series(data=self.solar.dc_tracker, index=self.date_range) * 60
        #  print(solar_series.max())
        #  solar_series[start_date:end_chart_date].plot(ylabel='KW', figsize=self.figsize)

    def bus_battery_plot(self, chart_days=0, num_buses=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        num_bus_types = bool(self.std_buses) + bool(self.art_buses) + bool(self.exp_buses)
        if num_buses: num_per_type = max([1,int(num_buses / num_bus_types)])
        else: num_per_type = 1

        # chart of battery percentage for buses
        std_bus_chart = self.std_buses[0:min(num_per_type, self.bus_nums['std'])]
        art_bus_chart = self.art_buses[0:min(num_per_type, self.bus_nums['art'])]
        exp_bus_chart = self.exp_buses[0:min(num_per_type, self.bus_nums['exp'])]

        # need to pivot bus_df because of how bus data is tracked

        self._bus_battery_df.loc[self.start_date:end_chart_date, std_bus_chart + art_bus_chart + exp_bus_chart].plot(ylabel='Battery %', figsize=self.figsize)

    def bus_battery_plot2(self, bus_name, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()


        self._bus_battery_df.loc[self.start_date:end_chart_date, bus_name].plot(ylabel='Battery %', figsize=self.figsize)

    def total_energy_consumption_plot(self, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        # bus energy consumption over time
        pd.Series(index=self.date_range, data=self.depot.electricity_usage_tracker['electricity_usage'])[self.start_date:end_chart_date].plot(ylabel='energy consumed (kwh)', figsize=self.figsize)

    def battery_pct_plot(self, chart_days=0):
        if chart_days: end_chart_date = self.start_date + datetime.timedelta(days=chart_days)
        else: end_chart_date = self.date_range.max()

        if self.battery: self.soc_tracker_series[self.start_date:end_chart_date].plot(ylabel='battery %', figsize=self.figsize)
        else: print('No battery to plot.')

    def all_depot_info(self):
        with sqlite3.connect(self._blocks_db) as con:
            query = '''SELECT depot, type, count(block) AS blocks FROM blocks GROUP BY depot, type'''
            depots = pd.read_sql(query, con, index_col=['depot','type'])
            return depots

    # ENERGY COST FUNCTIONS
    def energy_costs_monthly(self):
        print('Energy consumption and cost by month:')
        monthly_energy_consumption = self.hourly_energy_consumption['consumption_kwh'].resample('m').sum()
        monthly_energy_costs = (self.hourly_energy_consumption['energy_cost']).resample('m').sum()
        return pd.concat([self.monthly_energy_consumption, monthly_energy_costs], axis=1)

    def total_costs_plot(self):
        self.total_costs.plot(kind='bar')

    def chargers_max(self):
        '''
        Max number of simultaneous chargers in use
        '''
        return max(self.depot.charger_tracker)
    
    # OUTPUT REPORT HTML FUNCTION

    def make_report(self, output_folder):
        output_folder = os.path.join(os.getcwd(), output_folder)
        
        a = Airium()

        os.makedirs(output_folder, exist_ok=True)

        # copy css
        classless = os.path.join(package_dir,'sources','classless.css')
        shutil.copyfile(classless, os.path.join(output_folder,'classless.css'))

        # generate output plots and CSVs
        power_strings = self.power_plot(out=output_folder)
        self.bus_plot(out=output_folder)
        self.activity_tracker_df().to_csv(os.path.join(output_folder, 'activity_tracker.csv'))
        self.bus_activity_gantt(out=output_folder)
        self.full_blocks_tracked.to_csv(os.path.join(output_folder, 'full_blocks_tracked.csv'))


        overview_strings = [
            f"Depot: {self.depot_name}",
            f"Sim run time: {self.num_days} days", 
            f"Charger max power: {self.charger_power} kw",
            f"Number of chargers: {self.chargers}",
            f"Depot power supply: {self.depot_power_supply} kw",
            
        ]

        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t=f"Bussim: {self.depot_name} depot report")
                a.link(href=r'classless.css', rel="stylesheet")
            
            with a.body():
                with a.div():
                    a.h1(_t=f'Bus sim depot report: {self.depot_name}')
                with a.div():
                    a.h3(_t="Overview")
                    with a.ul():
                        for i in overview_strings:
                            a.li(_t=i)
                        a.li(_t="Bus count:")
                        with a.ul():
                            for i in self.bus_nums:
                                a.li(_t = i + ": " + str(self.bus_nums[i]))

                with a.div():
                    a.h3(_t="Depot power use")
                    a.a(_t="Load profile csv", href="powerplot.csv")
                    a.img(src="powerplot.png")
                    with a.ul():
                        for i in power_strings:
                            a.li(_t=i)
                
                with a.div():
                    a.h3(_t="Buses and blocks")
                    a.a(_t="Bus data csv", href="busplot.csv")
                    a.img(src="busplot.png")
                    a.a(_t="Bus Gantt activity data csv", href="activity_tracker.csv")
                    a.img(src="gantt.png")
                    a.h4(_t="Block success by bustype")
                    a.a(_t="Full tracked block data", href='full_blocks_tracked.csv')
                    a(self.blocks_bustype_table().reset_index().style.format().to_html())

                    if self.block_failures:
                        failures_df = pd.DataFrame(self.block_failures)
                        failures_df.to_csv(os.path.join(output_folder, 'block_failures.csv'))
                        with a.p():
                            a(str("Block failures reported: " + str(len(self.block_failures)) + "."))
                            a.a(_t="Block failure data.", href = "block_failures.csv")
                    else:
                        a.p(_t="No block failures.")
                
                with a.div():
                    a.h3(_t="Electricity costs")
                    a(self.total_costs_table.to_html())

                with a.div():
                    a.h3(_t="Other details")

                    
                    with a.p(_t="Full inputs:"):
                        with a.ul():
                            with a.li():
                                a.a(_t="Directory of sources including power rates and bus battery sizes.", href=os.path.join(package_dir, 'sources'))
                            for i in self.meta_data:
                                if i == 'self': continue
                                a.li(_t= i + ":" + str(self.meta_data[i]))




        
        html_path = os.path.join(output_folder, 'depot_report.html')
        with open(html_path, 'wb') as f:
            f.write(bytes(a))
        
        webbrowser.open('file://' + os.path.realpath(html_path))


full_sim = partial(BusSim, \
    start_date = '2022-09-05', num_days = 2, \
    charger_power = 150, \
    chargers = 500, depot_power_supply = 100000, \
    block_waittime = 15, \
    rate_type = 'tod_high', constrain_charging_power = False, \
    peak_constraint = 100, shoulder_constraint = 100, \
    battery_kwh = 0, \
    battery_hours = 0, \
    solar_kw = 0, \
    blocks_sqltable = 'blocks_split_6_Gen_1', \
    real_temp = False, \
    temp = 23, \
    run_until = 0, \
    bus_percentile = False, \
    depot_name = 'KB', \
    art_bus_num = 20, std_bus_num = 20, exp_bus_num = 0)

# function to run bussim using configuration file and produce report output.
def config_sim(scenario="DEFAULT", **keywords):
    # print(f'Running bussim for "{scenario}" scenario.')

    config_file = os.path.join(package_dir, 'sources', 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file)

    if not any([scenario == 'DEFAULT', config.has_section(scenario)]):
        print('Scenario not found. Run "config" command to ensure scenario exists. Quitting.')
        return
    
    # set data types for reading config file.
    cfg_types = {
    'str':['depot_name', 'blocks_sqltable', 'start_date', 'rate_type', 'bus_gen'],
    'int':['exp_bus_num', 'num_days', 'charger_power', 'chargers', 'depot_power_supply', \
           'art_bus_num', 'std_bus_num', 'block_waittime', 'peak_constraint', \
           'shoulder_constraint', 'battery_kwh', 'battery_hours', 'solar_kw', 'bus_batt_min', \
           'temp', 'run_until'],
    'float':['bus_percentile', 'usable_battery'],
    'boolean':['constrain_charging_power', 'real_temp', 'superblocks']
    }

    
    # parse all settings in config file and assign proper dtype
    bs_settings = {}

    for key in config[scenario]:
        if key in cfg_types['str']:
            bs_settings[key] = config[scenario].get(key)
        elif key in cfg_types['int']:
            bs_settings[key] = config[scenario].getint(key)
        elif key in cfg_types['float']:
            bs_settings[key] = config[scenario].getfloat(key)
        else:
            bs_settings[key] = config[scenario].getboolean(key)

    bs_settings.update(keywords)  # Update settings with any additional keywords.
   
    return BusSim(**bs_settings)

            


