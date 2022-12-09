#Contains a function which runs a binary file with arguments in the gem5 simulator and a script which calls the function with the name of the binary file and the arguments as command line arguments.

import subprocess
import sys
import os

#function which runs a binary file with arguments in the gem5 simulator
def run_se(binary_file_name, args=None):
    #if no arguments are given, run the binary file with no arguments
    if args is None:
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "run-program-se", binary_file_name])
    #if arguments are given, run the binary file with the given arguments
    else:
        #print what is being run
        print(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "run-program-se", binary_file_name, *args])
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "run-program-se", binary_file_name, *args])

#script which calls run_se with the name of the binary file and the arguments as command line arguments
if __name__ == "__main__":
    #take the name of the binary file as a command line argument
    binary_file_name = sys.argv[1]
    #take the arguments to pass to the binary file as a command line argument
    args = sys.argv[2:]
    #if args is an empty list, set it to None
    if len(args) == 0:
        args = None
    #run the binary file
    run_se(binary_file_name, args)