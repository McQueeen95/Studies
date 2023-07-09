// get the min array from 0 ;

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>


// int min(int startP, int endP,int A[])
// {
//     int mini = A[0];

//     for (int i = startP; i < endP; i++)
//     {
//         if (A[i] < mini)
//         {
//             mini = A[i];
//         }
//     }

//     return mini;
// }

int main(int argc, char **argv)
{

   // time_t startT = time(NULL);

    int myrank, size, start, end ,n;
    
    int arrM[4];

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (myrank == 0) // core 0 fills array1
    {
        scanf("%d", &n);

        
    }

    int arr[n];

    if (myrank == 0){
        for (int i = 0; i < n; i++)
        {
            // arr[i] = rand() % 10 + 1;
            arr[i] = i+2;
        }
    }

    int countOfNum = n / size;

    start = countOfNum * myrank;
    end = countOfNum * (myrank + 1);

    //int minimun = min(start, end);

    int minimum = arr[0];
    for (int i = start ; i < end ; i++){
        if(arr[i] < minimum){
            minimum = arr[i];
        }
    }




   // printf("hi i'm processor %d of %d and my minimum is :%d \n", myrank, size, minimum);

    // printf("\n");




    if (myrank != 0)
    {
        MPI_Send(&minimum, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    }
    else
    {
        for (int i = 1; i < size; i++)
        {
            MPI_Recv(&arrM[i-1], 4, MPI_INT, i, 1, MPI_COMM_WORLD, &status);
        }
    }

    if (myrank == 0)
    {
        int x = arrM[0];

        for (int i = 0; i < 4; i++)
        {
            if (arr[i] < x)
            {
                x = arr[i];
            }
        }

        printf("the min of all is: %d \n", x);
    }

    // time_t finishT = time(NULL);

    // double diff = difftime(finishT, startT);
    // printf("seconds spent of core %d is :%f \n", myrank, diff);

    MPI_Finalize();

    return 0;
}
