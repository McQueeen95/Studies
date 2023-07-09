#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv)
{
    time_t startS = time(NULL);
    int myrank, size, start, end, n = 8;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int countOfNum = n / size;

    int a[n], b[n], c[n];

    for (int i = 0; i < n; i++)
    {
        a[i] = rand() % 100 + 1;
        b[i] = rand() % 100 + 1;
    }

    // int a[] = {1, 2, 3, 4, 5, 6, 8, 7};
    // int b[] = {5, 6, 7, 8, 9, 10, 11, 12};

    start = countOfNum * myrank;
    end = countOfNum * (myrank + 1);

    printf("hi i'm processor %d of %d those my dot product : ", myrank, size);

    for (int i = start; i < end; i++)
    {
        c[i] = a[i] * b[i];
        printf("%d ", c[i]);
    }

    printf("\n");

    time_t finish = time(NULL);
    double diff = difftime(finish, startS);
    printf("and the second for prosessor number %d is %f seconds \n\n", myrank ,diff);


    MPI_Finalize();


    return 0;
}
