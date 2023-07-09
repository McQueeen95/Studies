#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int myrank, size, start, end, n = 100;
    double bigDeff ;
    MPI_Status status;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    double time_st = MPI_Wtime();

    int countOfNum = n / size;
    int sum = 0;

    start = countOfNum * myrank + 1;
    end = countOfNum * (myrank + 1);

    for (int i = start; i <= end; i++)
    {
        sum += i;
    }
    printf("hi i'm processor %d of %d and my sum is : %d \n", myrank, size, sum);

    double time_end = MPI_Wtime();
    double deff = time_end - time_st;

    // printf("time is : %f \n" , deff);
    /*if (myrank != 0)
        MPI_Send(&deff, 1, MPI_DOUBLE, 0, 1, MPI_COMM_WORLD);

    else
    {
        
        for (int i = 1; i < size; i++)
        {
            MPI_Recv(&bigDeff, 1, MPI_DOUBLE, i, 1, MPI_COMM_WORLD, &status);
            deff = deff + bigDeff;
        }
    }*/

    MPI_Barrier(MPI_COMM_WORLD);

    MPI_Reduce(&deff , &bigDeff , 1 , MPI_DOUBLE , MPI_SUM , 0 , MPI_COMM_WORLD);
    //printf("the total time is : %f", deff);

    if (myrank == 0)
        printf("the total time is : %f\n", bigDeff);

    MPI_Finalize();

    return 0;
}