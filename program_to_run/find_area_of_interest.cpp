//This program is designed to find the area of interest in the stats file by running a number of instructions designated by the user
//It is up to the user to check the stats file to see if the area of interest is correct
//For example, if the user runs with the argument "100" compared to "10", the number of instructions run will be approximately 10 times greater

#include <iomanip>
#include <iostream>

#include <gem5/m5ops.h>

using namespace std;

//basic function which runs a number of instructions designated by the user
void find_aoi(int num_instructions)
{
    for (int i = 0; i < num_instructions; i++)
    {
        cout << "0";
    }
}

int main(int argc, char *argv[])
{
    //check to see if the user entered an argument. If not, exit the program
    if (argc < 2)
    {
        cout << "Please enter a number of instructions to run\n";
        return 0;
    }
    //convert the argument to an integer
    int num_instructions = atoi(argv[1]);
    cout << "Beginning find area of interest program\n";

    m5_dump_reset_stats(0, 0);
    //run the function
    find_aoi(num_instructions);
    m5_dump_stats(0, 0);

}
