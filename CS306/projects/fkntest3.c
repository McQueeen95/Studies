#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <mpi.h>

using namespace std;
int main(int argc, char **argv)
{
    int size, myrank;
    int size_of_array;
    int array[100];
    // int new_array[10];

    int partial_sum;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);

    // cast the size of arraay to all nodes
    // split array and send to each noda

    if (myrank == 0)
    {

        cout << "enter the size of array";
        cin >> size_of_array;

        for (int i = 0; i < size_of_array; i++)
        {
            array[i] = i;
        }
    }
    MPI_Bcast(&size_of_array, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int size_send = size_of_array / size;
    int new_array[size_send];

    MPI_Scatter(array, size_send, MPI_REAL,
                new_array, size_send, MPI_REAL, //???? array or creat new_array??
                0, MPI_COMM_WORLD);

    for (int i = 0; i < 2; i++)
    {
        cout << "the process" << myrank << " " << new_array[i];
    }
    cout << "\n";

    int size_arr = size_of_array / size;

    // calculate partial sum for each noda
    for (int i = 0; i < size_arr; i++)
    {
        partial_sum += new_array[i];
    }
    cout << "\n"
         << partial_sum << "\n";

    int final_sum = 0;
    int sum_array[size];

    MPI_Gather(&partial_sum, 1, MPI_REAL,
               sum_array, 1, MPI_REAL, 0, MPI_COMM_WORLD);

    if (myrank == 0)
    {
        //  // the partial sum will save in array with order same rank
        for (int i = 0; i < size; i++)
        {
            cout << "\n"
                 << i << "calculate sum =" << sum_array[i] << "\n";
            //   final_sum+=sum_array[i];
        }
    }

    // or
    MPI_Reduce(&partial_sum, &final_sum, 1, MPI_REAL, MPI_SUM, 0, MPI_COMM_WORLD);

    if (myrank == 0)
    {
        cout << "\nthe final sum = " << final_sum << "\n";
    }

    MPI_Finalize();

    return 0;
}