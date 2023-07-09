#include <stdio.h>
#include <unistd.h>
#include <mpi.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
   int myrank, size ,start , end , n = 20;
  
   MPI_Init(&argc, &argv);
   MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);
  // printf("enter how many numbers u want : ");
  //scanf("%d" , n);

    int countOfNum = n / size;
   start = countOfNum * myrank + 1;
    end = countOfNum * (myrank + 1);

   printf("hi i'm processor %d of %d and i have those :  ", myrank, size);


   for(int i = 1; i <= countOfNum; i++)
        printf("%d ", myrank*countOfNum + i);

    printf("\n");

 
 

// int start = myrank*5 + 1 ;
// printf("processor %d displays : %d %d %d %d %d %d \n",rank,start,start+1,..,..,);


  MPI_Finalize();

   return 0;
}