import os
import configparser
import argparse
from subprocess import call
import bussim2.bussim as bs
import bussim2.minbus as mb

# func to load config for testing
config = None
def load_config():
    global config
    config = configparser.ConfigParser()
    config.read(config_file)

# TO DO: Create a default config file that can be reset?


package_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(package_dir, 'sources', 'config.ini')

parser = argparse.ArgumentParser(description='Command line interface for bussim2 module. This interface allows changing scenario configurations and producing bussim reports.')
parser.add_argument('command', metavar='<command>', help='"make_report": Produce bussim report; "min": Find minimum full service scenario for depot; "config": create or edit scenarios; "scenarios": list scenarios.')
parser.add_argument('-o', '--output', metavar='OUTPUT_DIRECTORY', dest='out_dir', help = 'Output directory for bussim report.')
parser.add_argument('-s', '--scenario', metavar='SCENARIO_NAME', dest='scenario', help="Choose scenario (after adding to bussim config) for running bussim. If no scenario is chosen, DEFAULT scenario will be used.")
parser.add_argument('-d', '--depot', metavar='DEPOT_NAME', dest='depot_name', help="Select depot for running 'min' function.")
args = vars(parser.parse_args())


# if command is make report, then make a report.
if args['command'] == 'make_report':
    
    # section to accept user input
    if not args['scenario']:
        print('Enter scenario (or hit Enter to use DEFAULT)')
        scenario_input = input()
        # if blank, use default, else change to input
        if scenario_input: 
            args['scenario'] = scenario_input
        else:
            args['scenario'] = 'DEFAULT'
    
    if not args['out_dir']:
        print('Enter output directory:')
        args['out_dir'] = input()
    
    if not args['out_dir']:
        print('Must specify output directory. Quitting.')
    else:
        bs.config_sim(args['scenario']).make_report(args['out_dir'])

# If command is "min", then run minimizer function
if args['command'] == "min":

    while not args['depot_name']:
        print('Enter depot code:')
        args['depot_name'] = input()
    
    else:
    
        if not args['out_dir']:
            print('Enter output directory:')
            args['out_dir'] = input()
        
        if not args['out_dir']:
            print('Must specify output directory. Quitting.')
        else:    
            min_report = mb.find_min_all(args["depot_name"])
            min_report.make_report(args['out_dir'])


# if command is config, open vim (or whatever the default editor is.)
if args['command'] == 'config':
    EDITOR = os.environ.get('EDITOR', 'vim')
    call([EDITOR, config_file])

if args['command'] == 'scenarios':
    load_config()
    print('Sections currently available in bussim config:')
    for i in ['DEFAULT'] + config.sections():
        print('  *',i)
    
