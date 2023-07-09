#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    
    int myrank, size, start, end, n, accum, sum;

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    if (myrank == 0)
    {
        // printf("enter how many numbers u want : ");
        scanf("%d", &n);
        for (int i = 1; i < size; i++)
            MPI_Send(&n, 1, MPI_INT, i, 2, MPI_COMM_WORLD);
    }
    if (myrank != 0)
        MPI_Recv(&n, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, &status);

    sum = 0;
    int countOfNum = n / size;
    start = countOfNum * myrank + 1;
    end = countOfNum * (myrank + 1);

    //   printf("hi i'm processor %d of %d :  ", myrank, size);

    for (int i = start; i <= end; i++)
        sum += i;

    //    printf("\n");

    if (myrank != 0)
    {
        MPI_Send(&sum, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    }
    else
    {
        for (int i = 1; i < size; i++)
        {
            MPI_Recv(&accum, 1, MPI_INT, i, 1, MPI_COMM_WORLD, &status);
            sum += accum;
        }
    }

    if (myrank == 0)
    {
        printf("the sum is: %d \n", sum);
    }

    MPI_Finalize();

    return 0;
}