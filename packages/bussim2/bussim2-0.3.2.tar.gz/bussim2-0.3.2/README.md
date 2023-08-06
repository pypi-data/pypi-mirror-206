# bussim2

[![PyPI - Version](https://img.shields.io/pypi/v/bussim2.svg)](https://pypi.org/project/bussim2)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bussim2.svg)](https://pypi.org/project/bussim2)

-----

**Table of contents**

[[_TOC_]]

## Installation

```console
pip install bussim2
```

## About

Bussim is a program created to estimate depot energy and power needs. It has been created to work with MTA data, but could be altered to accept data from other agencies. 

The program works by simulating realworld bus activity, simulated using the [SimPy Python module](https://simpy.readthedocs.io/en/latest/). SimPy is a "process-based discrete-event simulation framework based on standard Python." Buses are "dispatched" to run blocks (which are sequences of bus trips). Bus simulations are run for a predetermined period of time: They are given a real start date and a number of days to run for. Start dates should be in 2022, as the simulation loads the MTA's 2022 holiday calendar. The simulation also optionally loads real world hourly temperatures for 2022.

**Bus dispatches** occur based on provided block files, which are contained in bussim2/sources/blocks.db. Buses will only be dispatched for a particular block if they have enough battery state of charge to complete service. Any bus with enough available battery for a block can be dispatched, whether or not it is actively charging. Dispatch behavior can also be adjusted with an optional waittime paramter, to allow the dispatcher to either cancel a block immediately if no bus is available, or to wait for a given amount of time.

**Bus charging behavior** is meant to simulate realworld bus behavior. When buses get back to the depot, they either begin charging (with an optional buffer) or, if no chargers are available, they queue for a charger. 

**Bus charging speed** is limited by charger power, depot power supply and an optional peak time power constraint. If total charging speed exceeds depot power supply, busses will share available power equally. The simulation can also account for solar energy and energy storage installations that can be used to raise the maximum charging speed of the depot.

**Bus energy consumption** is determined by formulas included in bussim2/utilities.py. These formulas were calculated by performing nonlinear "MARS" regressions on real world std and art bus data, with energy consumption a function of block speed and outside temperature. This modeling work was done separately, and code is not contained in the bussim codebase.

## Running a simulation

The easiest way to create a bussim simulation and to view outputs is from the command line. After installing bussim2, a basic simulation can be run from the command line. The following command will generate a bussim report using the default configuration, will output a simulation report in the folder "report_dir", and will then open an HTML file with report details.

```console
% python -m bussim2 make_report -s DEFAULT -o OUTPUT_DIR
```

Scenarios can be configured for reports, and available scenarios can be listed, with with the following commands:

```console
% python -m bussim2 config    # configure bussim scenarios
% python -m bussim2 scenarios # view available scnearios
```

A minimization routine can be created using the following command. This routine finds the scenario for the given depot with the lowest possible number of buses, chargers, and power supply under which all block service can be fullfilled. The final resulting scenario will be the same as the output for a normal bussim. Note that running a minimization process can take around 10 minutes, as a few dozen bussim scenarios will be run to discover a working minimum scenario.

```console
% python -m bussim2 min -d DEPOT -o OUTPUT_DIR
```

While the command line is the easiest way to create bussim simulations, more powerful simulation analysis can be performed when bussim is used within an interactive python environment, especially within a Jupyter Notebook. Within a Python environment, the bussim program operates by creating "BusSim" objects that represent a self-contained simulation of a bus depot providing electric bus service.Objects are created by creating a new object with required arguments and assigning the object to a variable so that it can be accessed later. For example:

```python
import bussim.bussim as bs

# set variables
depot_name = "KB" #KB for Kinsbridge
num_days = 3
charger_power = 150
...

# create bus sim object
bus_sim = bs.BusSim([variables go here])

# optionally use a preconfigured scenario
bus_sim = bs.config_sim(scenario = "DEFAULT")

```

Once you have created a bussim object you can then generate plots or access details about its operation - such as the number of blocks that were run or failed, energy and power use for the depot, battery state of charge (SOC) for each bus, and more.

For example, to see how many blocks were run and dropped by type of bus, you could type:

```python
bus_sim.blocks_bustype_table()

                             num_blocks  miles_1000s  duration_hours
vehicle_type status                                                 
art          dropped_no_bus         612    18.089486     3260.800000
             run                     69     1.659155      271.516667
std          dropped_no_bus         603    20.437375     3471.633333
             run                     64     1.932952      293.716667
```

Methods for creating BusSim charts and plots include:
* BusSim.make_report(self, output_folder): Create a full HTML report and export to an output folder.
* BusSim.bus_activity_gantt(): View a gantt chart of bus activity.
* BusSim.bus_plot(self, chart_days=0, out=False): View a chart of bus activity throughout the simulation, including buses on blocks and buses charging.
  * chart_days: Change number of days represented in the chart.
* BusSim.power_plot(self, chart_days=0, out=False): View a plot of depot power by energy source.
* BusSim.bus_battery_plot(self, chart_days=0, num_buses=0): View a plot of bus battery state of charge over time.
* BusSim.bus_battery_plot2(self, bus_name, chart_days=0): View a plot of battery SoC for a specific bus.
* BusSim.battery_pct_plot(self, chart_days=0): View SoC for a depot's stationary battery.

Methods for generating output tables include:
* BusSim.def energy_costs_monthly(self): Generate a table of monthly energy and power costs for the depot.
* BusSim.blocks_bustype_table(self): Generate a table of blocks by bus type that ran or failed.
* BusSim.activity_tracker_df(self, buses=None, df=True): Generate a table of activity by bus, similar to data used for a Gantt chart.

## Optimizing depot infrastructure needs

One of the main functions of the bussim program is to find the minimum amount of infrastructure needed to maintain service: Number of buses, chargers, power supply, etc. The bussim program has a "minbus" program that can do this, given a depot. This can be run from the command line, as detailed above. Minbus functions can also be run within an interactive environment. This program operates using the "MIN" scenario contained in the bussim config file. Base settings can be altered in the config file, or by passing an "other_settings" option within python.


```python
import bussim2.minbus as mb

# run a minbus optimization process on the Kingsbridge depot.
min_sim = mb.find_min_all("KB")

# run a minbus process with a solar installation and higher speed chargers.
min_sim = mb.find_min_all("KB", other_settings = {'solar_kw': 500, 'charger_power':300})

# view number of buses, chargers, and power found by the minbus routine:
min_sim.num_buses
min_sim.chargers
min_sim.depot_power_supply
```


## Program structure and operation.

The following sections describe key files that govern the operation of the bussim program.

* bussim: Contains code for creating bussim objects. Each bussim object is a self-contained simulation, with methods and properties for viewing charts and data tables for the bussim.
* minbus: Contains code for running the minbus optimization.
* bussimclasses: Contains major classes representing real-world things: Ebus, depot, dispatcher, solar, battery.
* utilities: Utility functions for running the sim, primarily intangible functions such as block handling, determining utility TOUs, etc.
* sources/: Directory of data files used for running the sim, including all block data contained in blocks.db.

## License

`bussim2` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
