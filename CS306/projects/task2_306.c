#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int size;


void Ci_Arr(int arr[], int index)
{
   int ptr = fork();
   if (ptr == 0){
        for (int i = 0; i < index; i++)
    {
        arr[i] = rand() % 51 + 50;
    }

   }

   
}

int sum(int x[], int index)
{
int s =0;
    for (int i = 0; i < index; i++)
    {
        
        s +=x[i];
    }

    return s;
}

double average(int s, int index)
{
    return s / index;
}

int main()
{

    printf("Enter an integer plz: ");
    scanf("%d", &size);

    int array[size];

    Ci_Arr(array, size);

    FILE *output;
    output = fopen("shttt.txt", "w");

    for (int i = 0; i < size; i++)
    {
        fprintf(output, "%d\t ", array[i]);
    }

    int sumiton = sum(array, size);

    fprintf(output, "\nthe sum is : %d \n the average is : %d \n ",sumiton ,(sumiton/size) );

    fclose(output);

    return 0;
}