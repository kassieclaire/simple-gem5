//This is a simple matrix multiplication program that can be used to test the gem5 simulator.
//The original author of this program is Jason Lowe-Power
//The editor of this program is Justin Perona
//The repository is available here: https://github.com/jlpteaching/ECS201A/blob/master/hw2/hw2.rst
#include <iomanip>
#include <iostream>
#include <random>

#include <gem5/m5ops.h>

using namespace std;

#ifdef BLOCK_SIZE
void multiply(double **A, double **B, double **C, int size)
{
    for (int k = 0; k < size; k += BLOCK_SIZE) {
        for (int j = 0; j < size; j += BLOCK_SIZE) {
            for (int i = 0; i < size; i++) {
                for (int jj = j; jj < min(j + BLOCK_SIZE, size); jj++) {
                    #pragma unroll
                    for (int kk = k; kk < min(k + BLOCK_SIZE, size); kk++) {
                        C[i][jj] += A[i][kk] * B[kk][jj];
                    }
                }
            }
        }
    }
}
#else
void multiply(double **A, double **B, double **C, int size)
{
    for (int i = 0; i < size; i++) {
        for (int jj = 0; jj < size; jj++) {
            #pragma unroll
            for (int kk = 0; kk < size; kk++) {
                C[i][jj] += A[i][kk] * B[kk][jj];
            }
        }
    }
}
#endif

void printMatrix(double **A, int size)
{
    for (int i=0; i<size; i++) {
        for (int j=0; j<size; j++) {
            cout << setprecision(3) << setw(8) << A[i][j] << "  ";
        }
        cout << endl;
    }
}

int main(int argc, char *argv[])
{

    if (argc != 2) {
        cout << "Usage: mm size" << endl;
        return 1;
    }

    int size = atoi(argv[1]);

    if (size <= 0) {
        cout << "Invalid size" << endl;
        cout << "Usage: mm size" << endl;
    }

    cout << "Initalizing the matricies...";

    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0, 1);

    double *dataA = new double[size*size];
    double *dataB = new double[size*size];
    double *dataC = new double[size*size];

    double **A = new double*[size];
    double **B = new double*[size];
    double **C = new double*[size];

    for (int i = 0; i < size; i++)    {
        A[i] = &dataA[size*i];
        B[i] = &dataB[size*i];
        C[i] = &dataC[size*i];
        for (int j = 0; j < size; j++) {
            A[i][j] = dis(gen);
            B[i][j] = dis(gen);
            C[i][j] = 0;
        }
    }

    cout << "Done." << endl;

    cout << "Matrix A:" << endl;
    printMatrix(A, size);
    cout << "Matrix B:" << endl;
    printMatrix(B, size);

    cout << "Beginning multiply...";

    m5_dump_reset_stats(0, 0);
    multiply(A, B, C, size);
    m5_dump_stats(0, 0);

    cout << "Done." << endl;
    cout << "Matrix C:" << endl;
    printMatrix(C, size);

    delete[] A;
    delete[] B;
    delete[] C;
    delete[] dataA;
    delete[] dataB;
    delete[] dataC;

}
