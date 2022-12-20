//This is a simple hello world program that can be used to test the gem5 simulator.
//The author of this program is Kassie Povinelli
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
