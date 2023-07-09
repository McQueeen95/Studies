#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
#include <mpi.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{

  printf("bro u enterd %d numbers \n", argc - 1);

  // time_t start = time(NULL);
  // printf("%ld\n", start);

  double t_st = MPI_Wtime();

  int row = atoi(argv[1]);
  int column = atoi(argv[2]);

  //sleep(1);

  int a[row][column];
  int b[row][column];

  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < column; j++)
    {
      a[i][j] = rand() % 100 + 1;
      b[i][j] = rand() % 100 + 1;
    }
  }

  int c[row][column];

  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < column; j++)
    {

      c[i][j] = a[i][j] * b[i][j];
    }
  }

  /*time_t finish = time(NULL);
  printf("%ld\n", finish);

  double diff = difftime(finish, start);

  printf("%f second \n", diff);*/

  double t_ed = MPI_Wtime();

  double duration = t_ed - t_st;
  printf("total time is : %f \n" , duration);

  return 0;
}

// its runs to 835 ,, and after 836 its make segmentation fault
