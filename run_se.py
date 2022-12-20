#Contains a function which runs a binary file with arguments in the gem5 simulator and a script which calls the function with the name of the binary file and the arguments as command line arguments.
#notes: gem5 simulator arguments include:

import subprocess
import sys
import os

#function which runs a binary file with arguments in the gem5 simulator
def run_se(args):
    
    #print what is being run
    print(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "run-program-se", *args])
    subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "run-program-se", *args])

#script which calls run_se with the name of the binary file and the arguments as command line arguments
if __name__ == "__main__":
    #args is all arguments including the name of the file
    #the name of the file is indicated by a -b flag
    #the simulator arguments are before the -b flag
    #the binary file arguments are after the binary file name
    args = sys.argv[1:]
    #run the binary file
    run_se(args)