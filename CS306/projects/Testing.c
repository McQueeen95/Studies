// atoi() --> convert string into int and used in argv[] when we put arguments

#include "stdio.h"
#include <unistd.h>
//#include <mpi.h>
#include <stdlib.h>
#include <math.h>
#include <strings.h>

/* void test1 ( int m , int n){
     m =5;
     n = 24;
 }
 void test2 (int *m , int *n){
     *m = 5;
     *n  =24;
 }
 void test3 (int a , int *b){
     a = 38;
     *b = 57;
 }



int main(void){
 int a =10 , b = 16;

 printf("%d , %d \n" ,a,b);

 test1(a,b);
 printf("%d , %d \n" ,a,b);

test2(&a ,&b);
printf("%d , %d \n" ,a,b);

test3(a, &b);
printf("%d , %d \n" ,a,b);

return 0;*/

/*int myrank , size;
int main (int argc , char **argv)
{
 MPI_Init(&argc , & argv);
 MPI_Comm_rank(MPI_COMM_WORLD , &myrank);
 MPI_Comm_size(MPI_COMM_WORLD , &size);

 printf("processor %d of %d : hello world \n " , myrank , size );

 if (myrank %2 == 0 ) {
    printf ("hi bro i am even core \n ");
 }
  else {
  printf (" comen i am odd plz make me even \n ");
  }


     MPI_Finalize();*/

/*int main(){
    char a[]="ahmed";
    printf("%s\n" , a);
    char c = 'H';
    printf("%c\n", c);
    char b[] = {'H','i','\0'};
    printf("%s\n",b);


return 0


 }*/

/* int i =0;

int main(int argc, char **argv)
{

 MPI_Init(&argc, &argv);

     for ( ; i<5 ;i++){

         printf("%d\n",i);
         break;
     }
     printf("The Process %d", );

   MPI_Finalize();*/

/*int main()
{
    // int x =59;
    // int *pt;
    // pt= &x;
int x =5;
    int *ptr =&x;
    printf("hi : %d \n" , *ptr); // display the refernce of x 

    char wow[] = "Hillllo " ;
    char *yes = "wowowow";

    printf ("%s" ,&yes);


//    printf(" hi again : %d \n and it : %ld " , *pt , sizeof(pt)); // display the the value of x

  //  printf(fkn);

return 0;


     
}

*/

/*void main(void){
    int x = 0;
   
   
    if(1){
      printf("hi");


    }

    
}*/
/*int input;

int sum (int x){
    return x + input;
}

long double factorial(int n){
    if(n==0)
    return 1;
    else
    return factorial(n-1)*n;
}*/

/*int main(){
    long double a;
    scanf("%d",&input);
    a=factorial(input);

    printf("the fact of %d is %0.0Lf",input,a);

    return 0;
}*/

/*int main(int argc , char *argv[]){
    printf("this is first thing %d" ,atoi(argv[1]));
}*/

/*int main(){
    pid_t g = fork();
    printf("nice %d \n",g);

       if(g==0){
           printf("hi i'm child p2 %d\n",getpid());
           pid_t n = fork();
           if(n==0){
               printf("hi i'm p3\n");
               pid_t s = fork();
               if(s==0){
                   printf("hi i'm p4\n");
               }
               else{
                   printf("hi i'm p3 again\n");
               }
           }
           else{
               printf("hi i'm p2 again\n");
               pid_t t = fork();
               if(t==0){
                   printf("hi i'm p5\n");
               }
               else{
                   printf("hi i'm p2 again again\n");
               }
           }
       }
       else{
           wait(NULL);
           printf("hi i'm parent p1 %d\n",getpid());
           
       }


    return 0;
}*/
double randfrom(double min , double max){
    double range = (max - min);
    printf("%f\n",range);
    double div = RAND_MAX/range;
    printf("%f\n",div);
    double thing = rand();
    printf("%f\n",thing);
    double d = thing/div;
    printf("%f\n",d);
    double final = min + d ;

    return final;
}

int main(){
    double mr = randfrom(-1.0,1.0);
    printf("%f\n",mr);
}



















