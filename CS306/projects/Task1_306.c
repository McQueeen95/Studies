#include <stdio.h>
#include <stdlib.h>

int total, code, D1, D2, D3;
char name[10];

int sum(int x, int y, int z)
{
    return x + y + z;
}

int main()
{

    FILE *input, *output;

    input = fopen("shit.txt", "r");
    output = fopen("shitAfterShit", "w");

    fscanf(input, "%d", &total);

    for (int i = 1; i <= total; i++)
    {
        fscanf(input, "%s %d %d %d %d \n", &name, &code, &D1, &D2, &D3);

        fprintf(output, "%s\t%d\t %d\t %d\t %d \t %d \t", name, code, D1, D2, D3, sum(D1, D2, D3));

        if (sum(D1, D2, D3) < 150)
            fprintf(output, "congratulations u failled\n");

        else
            fprintf(output, "sad u passed :( \n");
    }
    fclose(input);
    fclose(output);
    return 0;
}