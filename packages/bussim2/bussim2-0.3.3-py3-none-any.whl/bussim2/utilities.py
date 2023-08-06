"""## Utility functions
* energy factor
* energy rates
* tou periods
"""

import math
import os
import datetime
import sqlite3
import pandas as pd
import statistics as s

package_dir = os.path.dirname(os.path.abspath(__file__))

# this equation applies a factor for any temperature. see appendix for chart. NOT IN USE YET
def energy_factor(temp):
    eq = lambda x: math.cos(x/15) / 5 + 0.8 - 0.001 * x
    limit = eq(30 * math.pi)
    return 1 if temp < 0 else eq(temp) if temp < 30 * math.pi else limit

def get_current_tou(start_date, now, tous):
    current_hour = (start_date + datetime.timedelta(minutes = now -1)).hour
    current_weekday = (start_date + datetime.timedelta(minutes = now - 1)).weekday()

    if current_weekday in [5, 6]:
        return 'all_else'

    for tou in tous:
        if current_hour in tous[tou]:
            return tou

# function to get energy rate
def get_energy_rate(month, dayofweek, hour, energy_rates):
    season = 'summer_june-july-august' if month in [6,7,8] else 'winter'
    tou = '8a-10p_m-f' if (dayofweek in range(5)) and (hour in list(range(8, 22))) else 'all_else'
    return energy_rates.loc[season, tou] / 100 # div by 100 to convert cents to dollars

"""The following code block takes block data (data for weekdays and weekends) and extrapolates it into a full calendar based on dates provided."""

class BlockData:
    '''Generate full set of block data for running a simulation. This class loads raw block data and then processes blocks based on service calendar and sim days.
    depot_data and service_cal must be correctly formatted Pandas DataFrames.'''

    service_cal = pd.read_csv(os.path.join(package_dir,'sources','service_calendar_simplified.csv'), parse_dates=[0], index_col=0)
    depot_info = pd.read_csv(os.path.join(package_dir,'sources','depot_info.csv'), index_col=0)

    def __init__(self, depot, start_date, blocks_db, blocks_table="blocks_originals", days=30, superblocks=False):
        self.depot = depot
        self.start_date = start_date
        self.days = days
        self.blocks_db = blocks_db
        self.entity = self.depot_info.at[self.depot, "entity"]
        self.blocks_table = blocks_table
        self.superblocks = superblocks

        # entity cal is the service calendar just for the relevant entity (mtabus or nyct)
        # note that the calendar has been simplified to strip out some small sub-entity differences between regions
        self.entity_cal = self.service_cal[(self.service_cal['entity'] == self.entity) & (self.service_cal['remove_to_simplify'] != True)].drop('remove_to_simplify', axis=1)
        
        # next lines run class methods to generate the sim calendar, load raw block data, and generate full blocks for running the sim.
        self.sim_cal = self.make_sim_calendar()
        self.blocks = self.get_block_data()

        # full blocks for use in sim
        self.full_blocks = self.make_full_blocks()
        self.full_blocks_df = pd.DataFrame(self.full_blocks).sort_values('dispatch_start_time').set_index('block_index')

        # get end time
        self.max_time = max([block['end_time'] for block in self.full_blocks])


    def get_day_type(self, dayofweek):
        if dayofweek in list(range(0,5)):
            return 'Weekday (school open)'
        elif dayofweek == 5:
            return 'Saturday'
        else:
            return 'Sunday'
        
    def make_sim_calendar(self, df=False):
        '''set df=True to return a dataframe of the calendar.
        This method generates a calendar that is then used to create a block schedule for running the bus sim.'''
        dates = pd.date_range(self.start_date, periods=self.days, freq="D")
        cal = [{'date':date, 'day':(date - pd.Timestamp(self.start_date)).days, \
                'dayofweek': date.dayofweek, 'day_type': self.get_day_type(date.dayofweek)} for date in dates]
        
        service_cal_dict = self.entity_cal.to_dict(orient='index')
        cal_dates = [x['date'] for x in cal]
        
        # loop through calendar and check for service adjustments
        for i in enumerate(cal):
            if i[1]['date'] in service_cal_dict.keys():
                pd_ts = pd.Timestamp(i[1]['date'])
                cal[i[0]] = {**i[1], **service_cal_dict[pd_ts]}
        if not df: 
            return cal
        else:
            return pd.DataFrame(cal)
    
    def get_block_data(self):
    # connect to blocks_db and select depot blocks
        with sqlite3.connect(self.blocks_db) as con:
            # Raise error if no blocks for depot.
            depot_query = f'SELECT DISTINCT depot FROM {self.blocks_table}'
            if self.depot not in pd.read_sql(depot_query, con).iloc[:,0].values:
                raise RuntimeError(f'No blocks found for depot {self.depot}.')
        
        # selecting only blocks without holiday codes
        query = fr'''
        SELECT * FROM {self.blocks_table} WHERE depot = "{self.depot}" AND holiday = " "
        '''
        raw_blocks = pd.read_sql(query, con)
        # Raise error if no blocks found because of some other potential issue.
        if raw_blocks.shape[0] < 1:
            raise RuntimeError(f'No blocks loaded from {self.blocks_db}')
        
        # process block data
        if not self.superblocks: # make old style blocks match superblocks columns
            raw_blocks['dispatch miles'] = raw_blocks['miles']
            raw_blocks['consumption miles'] = raw_blocks['miles']
            raw_blocks['consumption duration'] = raw_blocks['duration']
            raw_blocks['dispatch speed'] = raw_blocks['speed']
            raw_blocks['consumption speed'] = raw_blocks['speed']
            raw_blocks['start of consumption'] = raw_blocks['start']

            raw_blocks.drop(columns=['miles', 'speed'])


        block_dtypes = {'start':int, 'end': int, 'dispatch miles': float, 'consumption miles': float,\
                            'dispatch speed': float, 'consumption speed': float, 'consumption duration': int,
                            'duration': int, "start of consumption": int}

        
        blocks = raw_blocks[raw_blocks['depot'] == self.depot].astype(block_dtypes)
        # blocks['avg_speed'] = pd.to_numeric(blocks['avg_speed'])
        blocks['type'] = blocks['type'].str.lower()
        # blocks['duration_hours'] = blocks['duration'] / 60
               
        return blocks


    def make_full_blocks(self):
        '''Take depot blocks and generate a full set of blocks for the days that the sim takes place'''
       
        blocks_dict = self.blocks.to_dict(orient='records')

        full_blocks = []

        block_index = 0 # create a unique block index
        for block in blocks_dict:

            for day in self.sim_cal:
                if 'sched_to_apply' in day.keys():
                    sched_type = day['sched_to_apply']
                else:
                    sched_type = day['day_type']
                
                if sched_type != block['day']: continue # do not add block to full schedule if wrong service type
                                
                block_starttime = day['day'] * 1440 + block['start'] # 1440 is minutes in a day
                
                
                consumption_starttime = day['day'] * 1440 + block['start of consumption']

                if block_starttime <= 0: continue # do not add block if it starts before the simulation      

                block_times = {'dispatch_start_time': block_starttime, \
                               'consumption_start_time': consumption_starttime, \
                               'end_time': block_starttime + block['duration']}
                full_blocks.append({'block_index': block_index, **block, **block_times, **day})
                block_index += 1
        
        return full_blocks




"""### Energy cost functions"""

def calc_energy_costs(total_grid_demand,energy_rates):
    #convert to hourly consumption
    hourly_energy_consumption = total_grid_demand.resample('H').sum()
    hourly_energy_consumption = pd.DataFrame(data={'time': hourly_energy_consumption.index, 'consumption_kwh':hourly_energy_consumption.values})

    # apply electricity rate to each hour
    hourly_rates = hourly_energy_consumption.apply(lambda x: get_energy_rate(x.time.month, x.time.dayofweek, x.time.hour, energy_rates)[0], axis=1) # return [0] from get_energy_rate() to get energy charge.
    hourly_rates.name = 'energy_rate'

    # multiply rate by consumption to get energy cost
    hourly_energy_consumption = hourly_energy_consumption.join(hourly_rates)
    hourly_energy_consumption['energy_cost'] = hourly_energy_consumption['consumption_kwh'] * hourly_energy_consumption['energy_rate']
    hourly_energy_consumption.set_index('time', drop=True, inplace=True)
    return hourly_energy_consumption

"""Demand charge costs:

[Con ed PASNY rates](https://lite.coned.com/_external/cerates/documents/PSC12-PASNY/PASNYPSC12.pdf): "The total demand delivery charge for each billing period, excluding the Reactive Power Demand Charge, shall be the sum of the charges for each  applicable time period, each charge determined by multiplying the maximum demand for the respective time period by the rate applicable for that time period."

Therefore, the following code blocks find, by month, maximum 30-minute demand in KW for:
* 8am - 6pm
* 8am - 10pm
* all hours
"""

def calc_demand_costs(total_grid_demand, demand_rates, tou_days, tous, rate_type):

    # list all days
    days = total_grid_demand.index.to_timestamp().strftime('%Y-%m-%d').unique()

    peak_demand_tracker = []

    for day in days:
        day_minutely_energy = total_grid_demand[day] # convert back to kwh per minute
        #month = pd.Timestamp(day).strftime('%Y-%m')
        month = pd.Period(year = pd.Timestamp(day).year, month = pd.Timestamp(day).month, freq='M')
        season = 'summer_june-july-august' if pd.Timestamp(day).month in [6,7,8] else 'winter'
        day_num = pd.Timestamp(day).day

        if pd.Timestamp(day).dayofweek in tou_days['offpeak_days']:
            tou = 'all_else'
            tou_energy = day_minutely_energy
            tou_rolling_30min = tou_energy.rolling(window=30).sum()
            max_demand = tou_rolling_30min.max() * 2 #Times 2 to convert from kwh per 30 min to kw
            demand_rate = demand_rates.loc[season, tou, rate_type]['total_charge_usd_per_kw']
            demand_charge = max_demand * demand_rate

            peak_demand_tracker.append({'month': month, 'day': day, 'tou': tou, 'max_demand': max_demand, 'demand_rate': demand_rate, 'demand_charge': demand_charge})

        else:
            for tou in tous.keys():
                tou_energy = day_minutely_energy[day_minutely_energy.index.hour.isin(tous[tou])]

                tou_rolling_30min = tou_energy.rolling(window=30).sum()
                max_demand = tou_rolling_30min.max() * 2 #Times 2 to convert from kwh per 30 min to kw
                demand_rate = demand_rates.loc[season, tou, rate_type]['total_charge_usd_per_kw']
                demand_charge = max_demand * demand_rate

                peak_demand_tracker.append({'month': month, 'day': day, 'tou': tou, 'max_demand': max_demand, 'demand_rate': demand_rate, 'demand_charge': demand_charge})

    #peak_demand_df
    return pd.DataFrame(peak_demand_tracker)

'''
functions for calculating energy consumption per mile for buses. these are based on the MARS regression analysis run using R,
with some manual tweaks by Joseph.
'''


def f_std(mph, tmpf, perc=False):

    # cap mph at 95th % of sample
    mph = min(mph, 7.759866)

    # apply mars model
    consumption =   -18.56807 \
    +    4.913097 * max(0,      mph - 1.675203) \
    +   0.8289489 * max(0,      mph - 3.104523) \
    -   0.5421406 * max(0,      mph - 4.113259) \
    +    5.684302 * max(0, 5.656396 -      mph) \
    -    5.290822 * max(0,      mph - 5.656396) \
    +  0.06379681 * max(0,     62.5 -     tmpf) \
    +  0.05476839 * max(0,     tmpf -     62.5) \
    - 0.007598592 * max(0,      mph - 3.104523) * max(0,     tmpf -     63.5) \
    - 0.004243499 * max(0,      mph - 3.104523) * max(0,     63.5 -     tmpf) \
    +   0.0444514 * max(0, 5.656396 -      mph) * max(0,     tmpf -     81.5) \
    +   0.0103958 * max(0, 5.656396 -      mph) * max(0,     81.5 -     tmpf) \

    if perc: # if percentile given, add consumption figure to the estimate to estimate the Xth percentile of energy consumption
        min_var = 0.13442
        max_var = 0.76723
        intercept = -0.58814
        coef = 0.29735
        variance = min(max_var, max(min_var, intercept + coef * consumption))
        norm = s.NormalDist(mu = 0, sigma = variance ** 0.5)
        adder = norm.inv_cdf(perc)
        consumption += adder

    return consumption

def f_exp(mph, tmpf, perc=False, factor = 1.3):
    # express bus is simply the std energy consumption times a factor.
    consumption = f_std(mph, tmpf, perc)
    return consumption * factor

def f_art(mph, tmpf, perc = False):
    
    # cap mph at 95th % of sample
    mph = min(mph, 7.345454)
    
    # apply mars model
    consumption = -5.798385 \
    +   2.816288 * max(0,      mph - 1.931288) \
    +   3.187443 * max(0, 5.562491 -      mph) \
    -   2.702816 * max(0,      mph - 5.562491) \
    - 0.03845301 * max(0,     tmpf -       46) \
    +   0.127297 * max(0,     tmpf -     62.1) \
    +  0.1631874 * max(0,     66.2 -     tmpf) \
    - 0.04937138 * max(0,     tmpf -     66.2) \
    + 0.06959965 * max(0,     tmpf -       82) \
    -  0.1336557 * max(0, 1.774219 -      mph) * max(0,     66.2 -     tmpf) \
    - 0.01629277 * max(0,      mph - 1.774219) * max(0,     66.2 -     tmpf) \
    + 0.01646815 * max(0, 5.562491 -      mph) * max(0,     tmpf -     60.8) \
    -  0.0132295 * max(0,      mph - 5.562491) * max(0,     tmpf -       50) 

    # if percentile given, add consumption figure to the estimate to estimate the Xth percentile of energy consumption
    if perc: 
        min_var = 0.71722
        max_var = 1.94055
        intercept = -0.95466
        coef = 0.38668
        variance = min(max_var, max(min_var, intercept + coef * consumption))
        norm = s.NormalDist(mu = 0, sigma = variance ** 0.5)
        adder = norm.inv_cdf(perc)
        consumption += adder

    return consumption

def f_bus(gen, mph, tmpf, bustype, perc=False):
    gen_factor = {'gen_1':1, 'gen_2':.925, 'gen_3':.85}
    
    if bustype not in ['std', 'art', 'exp']: 
        raise Exception("bustype must be std, art, or exp")
    
    if bustype == 'std': return f_std(mph, tmpf, perc) * gen_factor[gen]
    if bustype == 'art': return f_art(mph, tmpf, perc) * gen_factor[gen]
    if bustype == 'exp': return f_exp(mph, tmpf, perc) * gen_factor[gen]
    
# get bus waittime shifting time to and from the chargers
buffer_times = pd.read_csv(os.path.join(package_dir,'sources', 'buffer_times.csv'), index_col=0).to_dict(orient='index')
def get_buffer(time):
    hour = (time / 60) % 24

    if hour > buffer_times['night']['hour_start']: #nightbuf
        return buffer_times['night']['buffer_time']
    elif hour > buffer_times['day']['hour_start']: #daybuf
        return buffer_times['day']['buffer_time']
    else: # morning
        return buffer_times['morning']['buffer_time']


# Help function to list tables in blocks.db

def list_sql_tables(blocks_db_file):
    with sqlite3.connect(blocks_db_file) as con:
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor = con.cursor()
        cursor.execute(sql_query)
        for i in cursor.fetchall():
            print(i[0])


