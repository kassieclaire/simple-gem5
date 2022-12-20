# imports
import os
import subprocess
import re
import platform
import shutil
import sys
import time

# defines
# git links
gem5_dev_git = "https://github.com/kassieclaire/gem5-dev.git"
# directories
gem5_wd = "gem5-wd"
gem5_dev = "gem5-dev"
# get current directory
cwd = os.getcwd()


# functions
# function to clone gem5-dev from github
def clone_gem5_dev():
    # clone the repository
    subprocess.run(["git", "clone", gem5_dev_git])

# function which checks if the system is running on an ARM machine
def is_arm():
    # use platform to get the architecture
    if platform.machine() == "arm64":
        return True
    return False

# function which fixes gem5 files to work with ARM
def fix_for_arm():
    # open the file to be fixed
    # the file is gem5-wd/source/src/arch/arm/kvm/gic.cc
    # replace the file with the fixed file, which is in the current directory and with the same name
    shutil.copyfile("gic.cc", "gem5-wd/source/src/arch/arm/kvm/gic.cc")

# function which starts docker if it's not already running
def start_docker():
    # if it's not running, start it
    # check if the machine is a linux machine -- if not, don't start docker
    if platform.system() == "Linux":
        subprocess.run(["systemctl", "--user", "start", "docker.service"])
#function to download the prebuilt gem5 simulator from the url and move it into the gem5-wd directory.
#the folder should be renamed to source
def download_gem5_simulator(url):
    #download the prebuilt gem5 simulator from the url
    subprocess.run(["wget", url])
    #get the name of the file
    file_name = url.split("/")[-1]
    #unzip the file
    subprocess.run(["unzip", file_name])
    #get the name of the folder
    folder_name = file_name.split(".")[0]
    #move the folder into the gem5-wd directory
    subprocess.run(["mv", folder_name, "gem5-wd/source"])
    #remove the zip file
    subprocess.run(["rm", file_name])
    

# Check for no-build and cslab arguments
# If no-build is present, don't build the gem5 simulator
no_build = False
# check if the no-build argument is present
if "--no-build" in sys.argv:
    no_build = True
    sys.argv.remove("--no-build")
# check if the csl argument is present. If it is true, run the docker engine start command
if "--csl" in sys.argv:
    # run the docker engine start command
    # the command is systemctl --user start docker.service
    print("Starting docker engine...")
    subprocess.run(["systemctl", "--user", "start", "docker.service"])
    # wait for the docker engine to start
    print("Waiting for docker engine to start...")
    # use python's sleep function to wait for 5 seconds
    time.sleep(5)
    sys.argv.remove("--csl")
# check if the fs argument is present. If it is, set the full system flag to true
full_system = False
if "--fs" in sys.argv:
    full_system = True
    sys.argv.remove("--fs")
#Check if download-prebuilt is present. If it is, download the prebuilt gem5 simulator from the link given (the argument after the flag)
download_prebuilt = False
prebuilt_link = ""
if "--d" in sys.argv:
    download_prebuilt = True
    # get the link to the prebuilt gem5 simulator
    prebuilt_link = sys.argv[sys.argv.index("--d") + 1]
    sys.argv.remove("--d")
    
# This is a script to prepare the gem5 simulator for full-system simulation
# It will download the gem5 simulator, set up a docker container, and build the simulator
# It will also download the disk image and kernel for the simulator

# first, check if user is running on an ARM machine. If they are, display a warning
if is_arm():
    # print a warning
    print("WARNING: You are running this script on an ARM machine. This script will work, but may produce unforseen results.")

# first, we need to build the docker container
# we will use the dockerfile in the gem5-dev directory
# we will name the container gem5-dev
# we will use the ubuntu:18.04 image
# we will use the gem5-wd directory as the working directory

# DIRECTORY SETUP
# check if the gem5-dev directory exists. If it does not, clone it from github
if not os.path.isdir("gem5-dev"):
    print("Cloning gem5-dev from github...")
    clone_gem5_dev()
# check if the gem5-wd directory exists. If it does not, create it
if not os.path.isdir("gem5-wd"):
    print("Creating gem5-wd directory...")
    os.mkdir("gem5-wd")

# DOCKER BUILD
# if docker is not running, start it

# change to the gem5-dev directory
os.chdir("gem5-dev")
# build the docker container
subprocess.run(["docker", "build", "-t", gem5_dev, "docker"])
# change back to the gem5 directory
os.chdir("..")

# SOURCE/SYSTEM INSTALL
# install the gem5 simulator source code
print("Installing gem5 source code...")
subprocess.run(["docker", "run", "--rm", "-v",
               f"{cwd}/{gem5_wd}:/gem5", "-it", gem5_dev, "install-source"])
# after gem5-source install, if detected host system is ARM, fix the gem5 source code
if is_arm():
    fix_for_arm()
# if full system is true, download the disk image and kernel
if full_system:
    # download the disk image and kernel using the install-system script
    print("Downloading disk image and kernel...")
    # use os.system instead of subprocess.run because the script is interactive
    os.system(
        f"docker run --rm -v \"{cwd}/{gem5_wd}:/gem5\" -it {gem5_dev} install-system")

# GEM5 BUILD
# build the simulator (currently set to ARM 4-core)
#Check that neither the no-build nor prebuilt argument is not present
if not (no_build or download_prebuilt):
    print("Building gem5 simulator...")
    subprocess.run(["docker", "run", "--rm", "-v",
                f"{cwd}/{gem5_wd}:/gem5", "-it", gem5_dev, "build"])
#check if the download-prebuilt argument is present. If it is, download the prebuilt gem5 simulator from the link given (the argument after the flag)
if download_prebuilt:
    print("Downloading prebuilt gem5 simulator...")
    download_gem5_simulator(prebuilt_link)
# TESTS
# perform a test-run of the simulator in syscall-emulation mode (hello world)
print("Performing test-run of gem5 simulator in se mode...")
subprocess.run(["docker", "run", "--rm", "-v",
               f"{cwd}/{gem5_wd}:/gem5", "-it", gem5_dev, "run-se"])
# perform a test-run of the simulator in full-system mode (hello world)
if full_system:
    print("Performing test-run of simulator in fs mode...")
    subprocess.run(["docker", "run", "--rm", "-v",
                   f"{cwd}/{gem5_wd}:/gem5", "-it", gem5_dev, "run-fs"])
