import shutil
import sys
import os
#This file contains a function which grabs the stats.txt file from the gem5 simulator and moves it to the stats directory.
#This file also contains a script which calls the function with the desired name of the stats file as a command line argument.

#define constants
path_to_stats = "gem5-wd/source/m5out/stats.txt"

#function which grabs the stats.txt file from the gem5 simulator and moves it to the stats directory and throws an error if the file doesn't exist
move_stats_file = lambda stats_file_name: \
    shutil.move(path_to_stats, 
                f"stats/{stats_file_name}") if os.path.exists(path_to_stats) else print("ERROR: stats.txt file not found. Have you run a new simulation?")

#script which calls the function with the desired name of the stats file as a command line argument
if __name__ == "__main__":
    #take the name of the stats file as a command line argument. If no argument is given, use the default name
    if len(sys.argv) == 1:
        stats_file_name = "stats.txt"
    else:
        stats_file_name = sys.argv[1]
    #move the stats file
    move_stats_file(stats_file_name)
