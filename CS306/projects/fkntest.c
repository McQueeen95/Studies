#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
int main(int argc, char *argv[])
{
    int n, div;
    double pi = 0, h, sump;
    int size, rank, start, end;
    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size); // get totalnodes
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0)
    {
        n = atoi(argv[1]);
    }
    double sttime = MPI_Wtime();
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    double endb = MPI_Wtime();
    start = (n / size) * rank;
    end = (n / size) * (rank + 1);
    h = (double)1 / n;
    for (int i = start; i < end; ++i)
    {
        pi += 4 * h / (1 + ((i * h) * (i * h)));
    }
    double strt = MPI_Wtime();
    MPI_Reduce(&pi, &sump, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    double endt = MPI_Wtime();
    if (rank == 0)
    {
        printf("sum of pi %f\n", sump);
        printf("total time = %f broadcast time =%f reduce time  %f \n", endt - sttime, endb - sttime, endt - strt);
    }
    MPI_Finalize();
    return 0;
}