#imports
import subprocess
import os
import sys
#Compiles the matrix multiplication program using the gcc-arm-linux-gnueabihf compiler

#function to compile a program using gcc given the name of the program
def compile_program(program_name, args=None):
    #copy the program from the program_to_run directory to the gem5-wd/source directory
    subprocess.run(["cp", f"program_to_run/{program_name}", "gem5-wd/source"])
    #run the compile-hello-world script in the gem5-dev docker container
    if args is not None:
        print(f"args: ${args}")
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "compile-program", program_name, *args])
    else:
        print("no args")
        subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "compile-program", program_name])
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