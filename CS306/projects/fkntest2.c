#include <mpi.h>
#include <cstdio>
#include <ctime>
#include <ratio>
#include <chrono>
#include <iostream>

using namespace std;

double calc_pi_part(double n, double i)
{
    double h = 1 / n;
    double nom = 4 * h;
    double dom = 1 + (i * h * i * h);
    return nom / dom;
}

int main(int argc, char *argv[])
{
    MPI_Init(&argc, &argv);
    double tot_st = MPI_Wtime();
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    int n;
    if (world_rank == 0)
    {
        printf("Enter a number: ");
        scanf("%d", &n);
    }
    MPI_Barrier(MPI_COMM_WORLD);
    double t_st = MPI_Wtime();
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    double t_ed = MPI_Wtime();
    double duration = t_ed - t_st;
    MPI_Barrier(MPI_COMM_WORLD);
    int st = world_rank * n / world_size + 1;
    int ed = (world_rank + 1) * n / world_size;
    if (world_rank == world_size - 1)
    {
        ed = n;
    }
    double part_pi = 0;
    for (double i = st; i <= ed; i++)
    {
        part_pi += calc_pi_part(n, i);
    }
    double pi = 0;
    MPI_Barrier(MPI_COMM_WORLD);
    t_st = MPI_Wtime();
    MPI_Reduce(&part_pi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    t_ed = MPI_Wtime();
    MPI_Barrier(MPI_COMM_WORLD);
    auto duration2 = t_ed - t_st;
    duration += duration2;
    double tot_ed = MPI_Wtime();
    double totTime = tot_ed - tot_st;
    if (world_rank == 0)
    {
        printf("n = %d , size %d\ntotal time %lf\ncomm time %lf\npi = %.6lf\n========\n",
               n, world_size,
               totTime, duration, pi);
    }
    MPI_Finalize();
}