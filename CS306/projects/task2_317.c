#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{

    printf("bro u enterd %d numbers and name of the file \n", argc - 2);

    time_t start = time(NULL);
    // printf("%ld\n", start);

    int **a = (int **)malloc((atoi(argv[1])) * sizeof(int *));

    int **b = (int **)malloc((atoi(argv[1])) * sizeof(int *));

    int **c = (int **)malloc((atoi(argv[1])) * sizeof(int *));

    for (int i = 0; i < atoi(argv[1]); i++)
    {
        *(a + i) = (int *)malloc((atoi(argv[2])) * sizeof(int));
        *(b + i) = (int *)malloc((atoi(argv[2])) * sizeof(int));
        *(c + i) = (int *)malloc((atoi(argv[2])) * sizeof(int));
    }

    for (int i = 0; i < atoi(argv[1]); i++)
    {
        for (int j = 0; j < atoi(argv[2]); j++)
        {
            (*(*(a + i) + j)) = rand() % 100 + 1;
            (*(*(b + i) + j)) = rand() % 100 + 1;
        }
    }

    for (int i = 0; i < atoi(argv[1]); i++)
    {
        for (int j = 0; j < atoi(argv[2]); j++)
        {
            (*(*(c + i) + j)) = (*(*(a + i) + j)) * (*(*(b + i) + j));
        }
    }

    FILE *output;

    output = fopen(argv[3], "w");

    for (int i = 0; i < atoi(argv[1]); i++)
    {
        for (int j = 0; j < atoi(argv[2]); j++)
        {
            fprintf(output, "C[%d][%d]= %d\n", i, j, (*(*(c + i) + j)));
        }
    }

    sleep(1);

    time_t finish = time(NULL);
    // printf("%ld\n", finish);

    double diff = difftime(finish, start);

    fprintf(output, "%f second spent \n", diff);

    fclose(output);

    for (int i = 0; i < atoi(argv[2]); i++)
    {
        free(*(a + i));
        free(*(b + i));
        free(*(c + i));
    }

    free(a);
    free(b);
    free(c);

    return 0;
}