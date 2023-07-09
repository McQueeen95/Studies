#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

pthread_mutex_t mutex;
pthread_cond_t cond0 , cond1;
int arr[];
int lnth;

int sum = 0;
float averge = 0;

void *fillArr(void *p){

     int Arry1[atoi(p)];
    
    int lnth = sizeof(Arry1) / sizeof(int);



    for (int i = 0; i < lnth; i++)
    {
        arr[i] = rand() % 10 + 1;
    }


}

void *sumi(void *p)
{
  pthread_mutex_lock(&mutex);
  pthread_cond_wait(&cond0,&mutex);
    for (int i = 0; i < lnth; i++)
    {
        sum += arr[i];
    }
    pthread_mutex_unlock(&mutex);
}

void *avg(void *p)
{
    pthread_mutex_lock(&mutex);
  pthread_cond_wait(&cond0,&mutex);
  averge = sum / lnth ;

   pthread_mutex_unlock(&mutex);

}


int main(int argc , char *argv[])
{
 
    scanf("%d" , &lnth);

    pthread_t thr1 , thr2 , thr3;
    pthread_mutex_init(&mutex,NULL);
    pthread_cond_init(&cond0,NULL);
    pthread_cond_init(&cond1,NULL);

    pthread_create(&thr1, NULL, fillArr, NULL);
    pthread_create(&thr2, NULL, sumi, NULL);
    pthread_create(&thr3, NULL, avg, NULL);

    pthread_join(&thr1,NULL);
    pthread_join(&thr2,NULL);
    pthread_join(&thr3,NULL);




     
    


}