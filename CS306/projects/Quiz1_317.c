#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

time_t startT = time(NULL);
	

int count , totalCount;
//int theNumber[50];


int checkPerfect(int n)
{
    int sum = 0;
    for (int i = 1; i < n; i++)
    {

        if (n % i == 0)
        {
            sum += i;
        }
    }
    if (sum == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void perfect(int startP, int endP)
{

    while (startP <= endP)
    {
        if (checkPerfect(startP))
        {
            theNumber[] = startP;

            printf("%d", startP);

            count++;
        }
        startP++;
    }
}

int main(int argc, char **argv)
{
    int myrank, size, start, end, n = 100;

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int countOfNum = n / size;

    start = countOfNum * myrank + 1;
    end = countOfNum * (myrank + 1);

    printf("hi i'm processor %d of %d  \n", myrank, size);
    printf("the perfect numbers between %d and %d is : \n", start, end);

    perfect(start, end);

    printf("\n");

    if (myrank != 0)
    {
        MPI_Send(&count, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
       // MPI_Send(theNumber, 1, MPI_INT, 0, 2, MPI_COMM_WORLD);
    }
    else
    {
        for (int i = 1; i < size; i++)
        {
            MPI_Recv(&totalCount, 1, MPI_INT, i, 1, MPI_COMM_WORLD, &status);
            count += totalCount;
            //MPI_Recv(&recNum, 1, MPI_INT, i, 2, MPI_COMM_WORLD, &status);
            
        }
    }

    if (myrank == 0)
    {
        printf("the count of all is: %d \n", count);
       // printf("the numbers is : %d" , recNum);
    }


    time_t finishT = time(NULL);

    double diff = difftime(finishT, startT);
    printf("seconds spent is :%f \n", diff);

    MPI_Finalize();

    return 0;
}
