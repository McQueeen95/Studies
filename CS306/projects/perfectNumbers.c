#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int counter ,iN , iNC=0;
int Arry[100];


int checkPerfect(int n)
{
    int sum = 0;
    for (int i = 1; i < n; i++)
    {

        if (n % i == 0)
        {
            sum += i;
        }
    }
    if (sum == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}


void perfect(int startP, int endP)
{
	
    while (startP <= endP)
    {
        if (checkPerfect(startP))
        {
        	++counter;
        	for (; iN < counter; iN++)
        	{
        		Arry[iN]=startP;
        	}
        	
            
        }
        startP++;
    }
}



int main(int argc, char *argv[])
{
	int arryM[100];
	MPI_Status status;
	int myrank,size,length=100;
	
	
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&myrank);//get rank
	MPI_Comm_size(MPI_COMM_WORLD,&size);//get total number of proccers
	int n=length/size;
	int start=(myrank*n)+1;
	int end=myrank*n+n;
	int sendNum=0;
	
	time_t now = time(NULL);
	perfect(start, end);



	if (myrank!=0)
	{
		MPI_Send(&counter,1,MPI_INT,0,1,MPI_COMM_WORLD);
		//MPI_Send(&iN,1,MPI_INT,0,1,MPI_COMM_WORLD);
		




		MPI_Send(Arry,counter,MPI_INT,0,1,MPI_COMM_WORLD);





		
	}else{
		for (int i = 1; i < size; i++)
		{
			MPI_Recv(&sendNum,1,MPI_INT,i,1,MPI_COMM_WORLD,&status);
			counter=counter+sendNum;
			// MPI_Recv(&iNC,1,MPI_INT,i,1,MPI_COMM_WORLD,&status);
			// iN=iN+iNC;
			MPI_Recv(arryM,100,MPI_INT,i,1,MPI_COMM_WORLD,&status);
			Arry[i]=arryM[i-1]; 








	
		}
		
	}
	if (myrank==0)
	{
		printf("\n %d\n",counter);
		for (int s = 0;s < size; s++)
		{
			printf("\n %d \n", Arry[s] );
		}
	}


	time_t se = time(NULL);
	long double x=difftime(se,now);
  	// printf("\nthe second is %Lf\n",x);




			// printf("\nmyRank=%d\n",myrank);
			// printf(" the number is %d \n",count );
		
	
			

	
	MPI_Finalize();
	return 0;
}