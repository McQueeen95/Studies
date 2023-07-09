#include <stdio.h>
#include <stdlib.h>
// #include <unistd.h>
// #include <time.h>
int main(int argc,char *argv[]){

    
//   if(argc == 1){
//   printf("please enter vlaue \n");
//   exit(0);

//   }

// time_t now =time(NULL);
// sleep(0);
int x= 1;
//int *ptr=(int*)x;
int *ptr1=&x;
printf("\n%ld\n",ptr1);
printf("%d\n",*ptr1);
int A[]={1,2,3,4,5};
int *ptrA=A;
int *ptr_A=&A[1];
printf("%ld\n",A);
printf("%ld\n",A+1);
printf("%ld\n",*(A+1));
printf ("%ld\n" , *A);
printf("%ld\n",ptrA);
printf("%ld\n",ptrA+1);
printf("%ld\n",*(ptrA+1));
printf("%ld\n",ptr_A);
int B[1][6]={{1,2,3,4,5,6}};
printf("%ld\n",B);
printf("%ld\n",(B+0)+1);
printf("%ld\n",(*(*(B+0)+1)));//A[0][1]

// time_t now_A =time(NULL);
// long double c=difftime(now_A,now);
// printf("\n%Lf\n",c);



    return 0;
}