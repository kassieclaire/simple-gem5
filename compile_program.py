#imports
import subprocess
import os
import sys
import platform
#Compiles the matrix multiplication program using the gcc-arm-linux-gnueabihf compiler

#function which checks if the system is running on an ARM machine
def is_arm():
    #use platform to get the architecture
    if platform.machine() == "arm64":
        return True
    return False

#function to compile a program using gcc given the name of the program
def compile_program(program_name, args=None):
    #copy the program from the program_to_run directory to the gem5-wd/source directory
    subprocess.run(["cp", f"program_to_run/{program_name}", "gem5-wd/source"])
    #select the correct compile script based on the architecture
    compiler = "cross-compile-program"
    if is_arm():
        compiler = "compile-program"
    
    #run the compile-hello-world script in the gem5-dev docker container
    if args is not None:
        print(f"args: ${args}")
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", compiler, program_name, *args])
    else:
        print("no args")
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", compiler, program_name])
#script which calls compile_program with the name of the program to compile 
if __name__ == "__main__":
    #take the name of the program to compile as a command line argument
    program_name = sys.argv[1]
    #take the arguments to pass to the compiler as a command line argument
    args = sys.argv[2:]
    #if args is an empty list, set it to None
    if len(args) == 0:
        args = None
    #compile the program
    compile_program(program_name, args)