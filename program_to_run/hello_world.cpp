//This is a simple hello world program that can be used to test the gem5 simulator.
//The original author of this program is 
//The editor of this program is Justin Perona
//The repository is available here: https://github.com/jlpteaching/ECS201A/blob/master/hw2/hw2.rst
#include <iomanip>
#include <iostream>

#include <gem5/m5ops.h>

using namespace std;

//basic hello world function
void hello_world()
{
    cout << "\nHello World\n";
}

int main(int argc, char *argv[])
{
    cout << "Beginning Hello World\n";

    m5_dump_reset_stats(0, 0);
    hello_world();
    m5_dump_stats(0, 0);

}
