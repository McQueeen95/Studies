#include <iostream>
using namespace std;

int main()
{
   /* int numOfPass;
   cin >> numOfPass;
   int result = 50 - (numOfPass%50);
    cout<<result<<endl; */
   /*int x = 6;
   while (x <= 10){
      cout << x <<endl;
      x++;
   }*/
   /*int i = 3 ;
   while (i <= 20){
      cout<<i<<endl;
      i+=3;
   }*/
   /*int sec;
   cin>>sec;
   while(sec >= 0){
      cout<<sec<<endl;
      sec--;
   }*/

   /*for(int i = 1 ; i <= 5 ; i++){
      cout<< 40*i << endl;
   }*/

   /*int purchaseAmount;
   double Price = 0.0;
   int i = 1;

   do
   {

      cin >> purchaseAmount;

      Price = purchaseAmount * 15 / 100;
      cout << Price << endl;
      i++;

   } while (i <= 3);*/

   /*int choice = 0;
   cin >> choice;
   switch(choice){
   case 1 : cout << "Latte" << endl;
   break;
   case 2 : cout << "Americano" << endl;
   break;
   case 3 : cout << "Espresso" << endl;
   break;
   case 4 : cout << "Cappuccino" << endl;
   break;
   case 5 : cout << "Macchiato" << endl;
   break;}*/

   
   /*int vision;
   cin >> vision;
   
   int height;
   cin >> height;
   
   if(vision==100 && height < 75 && height > 62)
      cout<<"passed"<<endl;
   else
      cout<<"failed"<<endl;*/

      /*double items[] = {500, 12.4, 94, 45, 3, 81, 1000.9, 85, 90, 1, 35};
      double discount;
      cin>>discount;

      for( int i =0; i < 11; i++){
         items[i]=items[i]-items[i]*(discount/100.0);
         cout<<items[i];
         cout<<" ";
      }*/

      /*string arr[3][3] = {
         {"Python", "JS", "C++"},
         {"PHP", "SQL", "Java"},
         {"C#", "Swift", "Kotlin"},
      };
      cout << arr[0][2];*/
      /*There are two operators for pointers:
Address-of operator (&): returns the memory address of its operand.
Contents-of (or dereference) operator (*): returns the value of the variable located
at the address specified by its operand.*/
      // int var = 50;
      // int *ptr = &var;

      // cout<<var<<endl; // 50(the value of var)
      // cout<<ptr<<endl; // refrence or the addres of var(variable that stores inside)
      //                  //var's memory location(refence)
      // cout<<*ptr<<endl;// 50(value of the variable  stored in the pointer ptr)

      /*int x = 5; //x=5
      int *p = &x;//*p=5 , p = ref of x

      x+=4; // x = 9 

      x = *p+4; // *p = 9 , x =13 */
      
      // int numOfRows;
      // cin >> numOfRows;

      // for(int l = 1 ; l <= numOfRows ;l++){
      //    for(int i = 1 ; i <= l ;i++){
      //    cout<<"*";
      //    }
      //    cout<<""<<endl;
      // }
      // cout<<"Done!"<<endl;
      // return 0;
      
      int x = 1;
      int y;
      y = (++x) + (x++);
      cout << y << " "  << endl;

}