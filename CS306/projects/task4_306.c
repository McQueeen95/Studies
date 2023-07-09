#include "stdio.h"
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

int n = 99999;
float meann;
int maxx = 0, minn;
int arr[1000000];


void *mean(void *p)
{
    int sum = 0;
    for (int i = 0; i <= n; i++)
    {
        sum += arr[i];
    }

    meann = sum / n;

    // pthread_mutex_lock(&mutex);
    // sleep(5);
    // // code

    // pthread_cond_signal(&cond);
    // pthread_mutex_unlock(&mutex);
}

void *max(void *p)
{
    for (int i = 0; i <= n; i++)
    {
        if (arr[i] > maxx)
        {
            maxx = arr[i];
        }
    }
}
void *min(void *p)
{
    minn = maxx;
    for (int i = 0; i <= n; i++)
    {

        if (arr[i] < minn)
        {
            minn = arr[i];
        }
    }
}

int main(int argc, char *argv[])
{

    pthread_t thr1;
    pthread_t thr2;
    pthread_t thr3;

    

    for (int i = 0; i <= n; i++)
    {
        arr[i] = rand() % 50 + 1;
    }

    

    //pthread_join(thr1, NULL);pthread_create(&thr1, NULL, mean, NULL);
    pthread_create(&thr2, NULL, max, NULL);
    pthread_create(&thr3, NULL, min, NULL);
    //(thr2, NULL);
    //pthread_join(thr3, NULL);

   // pthread_mutex_lock(&mutex);
    
    // waiting

    pthread_cond_wait(&cond, &mutex);
    // code
    pthread_mutex_unlock(&mutex);

    printf(" so the mean is %f \n and the maximum is %d \n and the minumum is %d \n", meann, maxx, minn);

    return 0;
}