#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
//#include<cmath>

double randfrom(double min , double max){
    double range = (max - min);
    double div = RAND_MAX/range;
    return min+(rand()/div);
}


int main(int argc, char **argv)
{
    int myrank, size, start, end;
    long int number_of_tosses, sum_of_cores, number_in_circle;
    double bigDeff;
    double PI;

    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    

    if (myrank == 0)
    {
        printf("Enter a number: ");
        scanf("%ld", &number_of_tosses);
        //number_of_tosses = atoi(argv[1]);
    }
    MPI_Barrier(MPI_COMM_WORLD);

    double time_st = MPI_Wtime();

    MPI_Bcast(&number_of_tosses, 1, MPI_INT, 0, MPI_COMM_WORLD);
    //MPI_Barrier(MPI_COMM_WORLD);

    int countOfNum = number_of_tosses / size;
    start = countOfNum * myrank + 1;
    end = countOfNum * (myrank + 1);

    
    srand(time(NULL));
    number_in_circle = 0;
    for (int toss = start; toss <= end; toss++)
    {
        double x = (double)rand()/RAND_MAX * 2.0 - 1.0;
        // double x2 = randfrom(-1.0,1.0);
       
        double y = (double)rand()/RAND_MAX * 2.0 - 1.0;

        
        
        double distance_squrared = (x * x + y * y);
        if (distance_squrared <= 1)
            number_in_circle++;
    
    //printf("\nthe x is %lf andy is : %lf \n" , x ,y );
    }

    

    double pi_estimate = (4 * number_in_circle) / ((double)number_of_tosses);

    MPI_Reduce(&pi_estimate, &PI, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    MPI_Reduce(&number_in_circle, &sum_of_cores, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (myrank == 0)
    {
        printf("the total num of circle is : %ld\n", sum_of_cores);
        printf("the PI is : %f\n", PI);
    }

    double time_end = MPI_Wtime();
    double deff = time_end - time_st;

    MPI_Barrier(MPI_COMM_WORLD);

    MPI_Reduce(&deff, &bigDeff, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (myrank == 0)
        printf("the total time is : %f\n", bigDeff);

    MPI_Finalize();

    return 0;
}