# README for GEM5 Simulator CLI Interface

## Project Description
This project aims to provide a user-friendly command line interface (CLI) for the GEM5 simulator, which is a popular open-source system-level simulator for computer architecture research. The CLI allows users to easily compile and run their own programs on the GEM5 simulator, as well as retrieve simulation statistics for analysis.

## System Requirements
- At least 8GB of RAM
- Docker Desktop
- Either an ARM (e.g. Apple M1) or x86 machine
- 10 GB of storage free (this will not all be used necessarily)
- A fast internet connection
- Git
- Python3

**Note:** If you are running this on a CSL machine, you can disregard the above system requirements.

## Preparing GEM5
To get started with the GEM5 simulator, follow these steps:

1. Clone the project into your desired directory:
```
git clone https://github.com/kassieclaire/simple-gem5.git
```
2. Navigate to the cloned project directory and run the `prepare_gem5.py` script:
```
cd simple-gem5
python3 prepare_gem5.py
```
If you are running this on a CSL machine, use the `--csl` argument:
```
python3 prepare_gem5.py --csl
```
If GEM5 is already built, use the `--nobuild` argument to skip the build process:
```
python3 prepare_gem5.py --nobuild
```
## Compiling a Binary
To compile a binary for use in the GEM5 simulator, follow these steps:

1. Simple C and C++ programs can be cross-compiled (on x86 machines) or compiled directly (on ARM machines) through the docker container. Make sure that the program includes the `<gem5/m5ops.h>` header and checkpoints. Examples of checkpoint use can be found in the `hello_world.cpp` and `mm.cpp` files.

2. Place the program file in the `program_to_run` directory.

3. Run the `compile_program.py` script with the program name (including extension) as the argument:
```
python3 compile_program.py hello_world.cpp
```
4. If there are no errors, the binary will now be in the `gem5_wd/source` directory.

## Running a Binary
This tool can run programs in syscall-emulation mode. Full-system emulation is currently in development.

To run a binary in the GEM5 simulator, use the `run-se` script with the following arguments:

1. Simulator options, which are read before the `-b` flag. These include cache configurations, core configurations, and other options determined by the GEM5 simulator. See the GEM5 documentation for more information.

2. Binary filename, which is read directly after the `-b` flag. This is the name of the binary you want to run.

3. Arguments for the binary, which are read after the binary filename.

For example, to run the `hello_world` binary with the default simulator options:
```
python3 run_se.py -b hello_world
```
## Getting Statistics
After running a syscall emulation simulation, GEM5 produces a statistics file containing values such as the number of CPU cycles simulated, the instruction count, and various more detailed statistics.

1. To move this statistics file after a syscall-emulation run to the /stats directory, run the get_statistics.py script.

2. Use the process_stats.py script to gather basic information about the simulation, including cycle count, instruction count, and simulator operations count.

To gather more information see the stats.txt file in the stats directory. Check the process_statss.py file for how the output is tokenized and processed for integer values -- different tokenization will be needed for float values.

## Maintenance and Expansion
Some key files to note for maintenance and expansion of this project include:
- gem5-dev.sh, which is a shell script in the gem5-dev/docker directory. This includes scripts that run inside the docker container.
- The dockerfile, which includes the setup for the Ubuntu 18.04 container and is also in the gem5-dev/docker directory.
## Credits
- Credit to ArturKlauser who worked on the original gem5-dev script implementation for setting up and running ARM simulations in a GEM5 docker image.
- Credit to Jason Lowe-Power and Justin Perona for the original version of the matrix-multiplication program for GEM5.
