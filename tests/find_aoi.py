#This is a script which runs the find_area_of_interest binary file using the run_se.py script.
#After running the run_se script, run the get_stats.py script to get the stats from the simulation.
#After running the get_stats script, run the process_stats.py script to process the stats.

#imports
import subprocess
import sys
import os
#import run_se function from run_se.py
from run_se import run_se

#run the find_area_of_interest binary file with the arguments given as command line arguments
run_se(["-b", "find_area_of_interest", *sys.argv[1:]])
#after running the binary file, run the get_stats.py script to get the stats from the simulation
subprocess.run(["python3", "get_stats.py"])
#after running the get_stats.py script, run the process_stats.py script to process the stats
subprocess.run(["python3", "process_stats.py"])
