#include <signal.h>
#include <stdio.h>


int timerf = 0;
void alarmHandler() {
	printf("alarm recieved\n");
	timerf = 1;
}

void handleSigInt() {
	puts("you can't kill me");
}

int main () {

	alarm(1);

	
	int (*handler)();
	int (*handler2)();
	handler2 = signal(SIGALRM,alarmHandler);
	handler = signal(SIGINT,handleSigInt);
	while(timerf == 0);
	alarm(1);

	printf("alarm 1 i am running forever %d \n" , getpid());
	signal(SIGINT,handler);
	signal(SIGALRM,SIG_IGN);
	int i = 1 , c = 0;
	while(i++ && c == 0){
		if ( i == 0 ) c+= 1;
	}
	alarm(2);

	signal(SIGALRM,SIG_DFL);
	
	i = 1 , c = 0;
	while(1);
	printf("never excute\n");
	
 }

