#imports
import subprocess
import os
#Compiles the matrix multiplication program using the gcc-arm-linux-gnueabihf compiler

#function to compile the a program using the gcc-arm-linux-gnueabihf compiler given the name of the program
def compile_mm(program_name):
    #copy the program from the program_to_run directory to the gem5-wd/source directory
    subprocess.run(["cp", f"program_to_run/{program_name}", "gem5-wd/source"])
    #run the compile-mm script in the gem5-dev docker container
    subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "compile-mm"])
#function to compile a program using gcc given the name of the program
def compile_program(program_name):
    #copy the program from the program_to_run directory to the gem5-wd/source directory
    subprocess.run(["cp", f"program_to_run/{program_name}", "gem5-wd/source"])
    #run the compile-hello-world script in the gem5-dev docker container
    subprocess.run(["docker", "run", "--rm", "-v", f"{os.getcwd()}/gem5-wd:/gem5", "-it", "gem5-dev", "compile-hello-world"])
#script which calls compile_program with the name of the program to compile 
if __name__ == "__main__":
    compile_program("hello_world.cpp")