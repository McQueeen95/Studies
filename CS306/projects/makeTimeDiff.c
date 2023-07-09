#include <stdio.h>
#include <time.h>
#include <unistd.h>
int main(){
  
  time_t now = time(NULL);

  printf("%ld \n" ,now);
 
  sleep(3);

  time_t after3 = time(NULL);

  printf("%ld \n" ,after3);

  double diff = difftime(after3,now);

  printf("%f \n" ,diff);

  char *time_now = ctime(&after3);

  printf("%s \n" , time_now);
  struct tm *gm_time = gmtime(&after3);

  printf("%d \n" , gm_time -> tm_sec);
  printf("%d \n" , gm_time -> tm_wday);
  printf("%d \n" , gm_time -> tm_mday);
  printf("%d \n" , gm_time -> tm_yday);
  printf("%d \n" , gm_time -> tm_hour);

  printf("\n");

   struct tm *local_time = localtime(&after3);

  printf("%d \n" , local_time -> tm_sec);
  printf("%d \n" , local_time -> tm_wday);
  printf("%d \n" , local_time -> tm_mday);
  printf("%d \n" , local_time -> tm_yday);
  printf("%d \n" , local_time -> tm_hour);
  return 0;
  

}