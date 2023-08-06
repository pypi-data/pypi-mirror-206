'''
program to find minimum number of buses that can fulfill depot blocks
'''

import sqlite3
import os
#from IPython.display import # clear_output
from functools import partial
import bussim2.bussim as bs
import matplotlib.pyplot as plt
import pandas as pd
import importlib

package_dir = os.path.dirname(os.path.abspath(__file__))

# get bus depot info
def get_all_depot_info(blocks_db = os.path.join(package_dir, 'sources', 'blocks.db')):
    with sqlite3.connect(blocks_db) as con:
        query = '''SELECT depot, type FROM 'blocks_split_MARS_Gen_1' GROUP BY depot, type'''
        depots = pd.read_sql(query, con, index_col=['depot'], columns='type')
        depot_types = depots.groupby('depot').agg(lambda x: [i.lower() for i in x])['type']
        return depot_types

# partial bussim with defaults filled out.
bus_test_sim = partial(bs.config_sim, scenario="MIN")

# find minimum bus just for one bus type
def find_min_bus_by_type(depot, bus_type, start_num, other_settings={}):
    
    # other settings
    bs_params = {'charger_power':150, 'chargers':500} # start with defaults
    bs_params.update(other_settings) #update with any other settings
    
    # bus settings
    bus_nums = {'std':0, 'art': 0, 'exp': 0}
    bus_nums[bus_type] = start_num

    std_bus_num = bus_nums['std']
    art_bus_num = bus_nums['art']
    exp_bus_num = bus_nums['exp']
    
    # set starting bus nums
    if bus_type == 'std': std_bus_num = start_num
    elif bus_type == 'art': art_bus_num = start_num
    elif bus_type == 'exp': exp_bus_num = start_num  
    
    # set test mode to begin bus min function
    test_mode = 'run1'
    bus_shortage_found = False
    while True:
        std_bus_num = bus_nums['std']
        art_bus_num = bus_nums['art']
        exp_bus_num = bus_nums['exp']
        bus_sim = bus_test_sim(depot_name=depot, std_bus_num=std_bus_num, art_bus_num=art_bus_num, exp_bus_num=exp_bus_num, **bs_params)

        if (bus_type, 'dropped_no_bus') in bus_sim.blocks_bustype_table().index and test_mode == 'run1':
            # clear_output(wait = True)
            print(bus_type, bus_nums[bus_type])
            bus_nums[bus_type] += 10
            bus_shortage_found = True
        elif ((bus_type, 'dropped_no_bus') not in bus_sim.blocks_bustype_table().index and test_mode == 'run1'):
            # clear_output(wait = True)
            print(bus_type, bus_nums[bus_type])
            if bus_shortage_found or bus_nums[bus_type] == 10:
                bus_nums[bus_type] -= 9
                test_mode = 'run2'
            else:       # this line is in case you start with an overestimate
                bus_nums[bus_type] -= 10
        elif (bus_type, 'dropped_no_bus') in bus_sim.blocks_bustype_table().index and test_mode == 'run2':
            # clear_output(wait = True)
            print(bus_type, bus_nums[bus_type])
            bus_nums[bus_type] += 1
        else:
            # clear_output(wait = True)
            print('Min bus found:', bus_type, bus_nums[bus_type])
            return {'bus_min': bus_nums[bus_type], 'bus_sim': bus_sim}

# Find min buses for depot and return a sim with all buses running.
def find_min_buses(depot, starting_guess = 80, other_settings = {}):
    depot_types = get_all_depot_info()[depot]
    results = {'std': 0, 'art': 0, 'exp': 0}
    print('Finding minimum buses to complete all blocks for', depot)
    for i in depot_types:
        result = find_min_bus_by_type(depot, i, starting_guess, other_settings=other_settings)
        results[i] = result['bus_min']
    # clear_output(wait = True)
    print('Generating minimum bus sim:', str(results),)
    
    # test to ensure all blocks running; if not add 1 bus at a time to everything    
    while True:
        print('testing min buses for', str(results))
        bus_sim = bus_test_sim(depot_name=depot, std_bus_num=results['std'], art_bus_num=results['art'],\
                               exp_bus_num=results['exp'], **other_settings)
        statuses = bus_sim.blocks_bustype_table().index.get_level_values(level=1)
        if 'dropped_no_bus' in statuses:
            for i in depot_types:
                results[i] += 1
        else:
            return bus_sim




def find_min_chargers(depot, bus_nums, chargers_start_num=20, charger_power=150):
    '''
    bus_nums formatted like: {'std':0, 'art': 0, 'exp': 0}
    '''
    chargers = chargers_start_num

    std_bus_num = bus_nums['std']
    art_bus_num = bus_nums['art']
    exp_bus_num = bus_nums['exp']
    
    # set test mode to begin bus min function
    test_mode = 'run1'
    charger_shortage_found = False

    print('Finding min chargers for',depot,bus_nums)
    while True:
        bus_sim = bus_test_sim(depot_name=depot, std_bus_num=std_bus_num, art_bus_num=art_bus_num, exp_bus_num=exp_bus_num, charger_power=charger_power, chargers=chargers)
        statuses = bus_sim.blocks_bustype_table().index.get_level_values(level=1)

        if 'dropped_no_bus' in statuses and test_mode == 'run1':
            # clear_output(wait = True)
            print('chargers:', chargers)
            chargers += 10
            charger_shortage_found = True
        elif 'dropped_no_bus' not in statuses and test_mode == 'run1':
            # clear_output(wait = True)
            print('chargers:', chargers)
            if charger_shortage_found:
                chargers -= 9
                test_mode = 'run2'
            else:       # this line is in case you start with an overestimate
                chargers -= 10
        elif 'dropped_no_bus' in statuses and test_mode == 'run2':
            # clear_output(wait = True)
            print('chargers:', chargers)
            chargers += 1
        else: # if run mode is run2 and no dropped buses, then you've found the min charger count
            # clear_output(wait = True)
            print('Min chargers found:', chargers, str(bus_nums))
            return {'charger_min': chargers, 'bus_sim': bus_sim}


def find_min_bus_and_chargers(depot, charger_power=150):
    min_bus_result = find_min_buses(depot, charger_power=charger_power)
    min_charge_result = find_min_chargers(depot, min_bus_result.bus_nums, charger_power=charger_power)
    return min_charge_result




# right now this only really works for chargers, power supply, and peak constraint.
# could be easily modified or tested to work with other things too.
def find_min_input(depot, input, bus_nums, other_settings={}):
    '''
    bus_nums formatted like: {'std':0, 'art': 0, 'exp': 0}
    starting inputs is object like {'chargers': 20, 'depot_power_supply': 10000}, etc.
    '''

    defaults = {'chargers': {'default': 500, 'starter': 30, 'step_x': 1},
                # 'charger_power': {'default': 150, 'starter': 150, 'step_x': 5},
                'depot_power_supply': {'default': 100000, 'starter': 4000, 'step_x': 100},
                'peak_constraint': {'default': 1000, 'starter': 1000, 'step_x': 100}
                }

    if input not in defaults.keys():
        raise Exception(f'Input must be in {defaults.keys()}')


    bs_params = {'depot_name': depot}
    
    # add default values to bs_params
    for i in defaults:
        bs_params[i] = defaults[i]['default']
    
    # add bus nums to bs_params
    for i in bus_nums:
        bs_params[i + '_bus_num'] = bus_nums[i]

    # update bs_params with any starting input settings
    bs_params.update(other_settings)
    bs_params[input] = defaults[input]['starter'] # set the optimizer to start at a reasonable starting value

    # set test mode to begin bus min function
    test_mode = 'run1'
    shortage_found = False

    print(f'Finding min {input} for',depot,bus_nums)
    while True:
        
        bus_sim = bus_test_sim(**bs_params)
        statuses = bus_sim.blocks_bustype_table().index.get_level_values(level=1)

        if 'dropped_no_bus' in statuses and test_mode == 'run1':
            # clear_output(wait = True)
            print(input, bs_params[input])
            bs_params[input] += 10 * defaults[input]['step_x']
            shortage_found = True
        
        elif 'dropped_no_bus' not in statuses and test_mode == 'run1':
            # clear_output(wait = True)
            print(input, bs_params[input])
            # if there's a shortage, or if you're at the minimum level, then subtract 9 and
            # start looking at small increments to get minimum
            if shortage_found or bs_params[input] == 10 * defaults[input]['step_x']:
                bs_params[input] -= 9 * defaults[input]['step_x']
                test_mode = 'run2'
            else:       # this line is in case you start with an overestimate
                bs_params[input] -= 10 * defaults[input]['step_x']
        
        elif 'dropped_no_bus' in statuses and test_mode == 'run2':
            # clear_output(wait = True)
            print(input, bs_params[input])
            bs_params[input] += defaults[input]['step_x']
       
        else: # if run mode is run2 and no dropped buses, then you've found the min charger count
            # clear_output(wait = True)
            print('Min found:', input, bs_params[input], str(bs_params))
            return bus_sim

def find_min_all(depot, other_settings={}, return_params = False):


    min_bus_result = find_min_buses(depot, other_settings=other_settings)
    
    bus_nums = min_bus_result.bus_nums
    min_charge_result = find_min_input(depot, 'chargers', bus_nums=bus_nums, other_settings=other_settings)
    
    other_settings.update({'chargers': min_charge_result.chargers})
    min_power_result = find_min_input(depot, 'depot_power_supply', bus_nums=bus_nums, other_settings=other_settings)

    # field names: 'depot,std,art,exp,chargers,depot_power_supply\n'
    params = [depot, bus_nums['std'], bus_nums['art'], bus_nums['exp'], min_power_result.chargers, min_power_result.depot_power_supply]
    
    if return_params:
        return params
    else:
        return min_power_result