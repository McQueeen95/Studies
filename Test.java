


public class Test{

  public static int[] col = new int[4];
  public static void main(String[] args){
    // queens(0,4);
    int[] x = {1,2,3,4,5,6,7,8,9,10};
    System.out.println(location(x, 0, x.length-1,9));
  }

  
  public static boolean promising(int i){
    int k = 1; 
    boolean Dis = true;
    
    while(k<i && Dis){
      if(col[i] == col[k] || col[i]-col[k]==i-k){
        Dis = false;
        k++;
      }
    }
    return Dis;
  }
  public static void queens(int i , int n){
    if(promising(i)){
      if(i==n){
        for(int x = i ; x <= n ; x++){
          System.out.println(col[x]);
        }
      }
      else{
        for(int j = 1 ; j <= n ; j++){
          col[i+1]= j;
          queens(i+1, n);
        }
      }
    }
  }
  public static int location(int[] arr ,int low , int high, int x){
    int mid = (int)Math.ceil((low+high)/2);
    if(low>high)
      return -1;
    else{
      if(x==arr[mid]){
        return mid;
      }
      else if(x < arr[mid]){
        return location(arr, low, mid-1, x);
      }
      else{
        return location(arr, mid+1, high, x);
      }
    }
  }
  public static int bin2(int n , int k){
    int[][] Arr = new int[n+1][k+1];
    for(int i = 0 ; i <= n+1 ; i++){
      for(int j = 0 ; j <= Math.min(i, k); j++){
        if(j==0 || i == j){
          Arr[i][j] = 1;
        }
        else{
          Arr[i][j] = Arr[i-1][j-1] + Arr[i-1][j];
        }
      }
    }
    return Arr[n][k];
  }



}