//PE46

public class PE0046{
  public static void main(String[] args){
    boolean done = false;
    int k = 3;
    while(!done){
      boolean flag = false;
      if(!isPrime(k)){
        for(int i = 1; i < Math.sqrt(k/2.0); i++){
          if(isPrime(k - 2 * i * i)){
            flag = true;
            break;
          }
        }
        if(!flag){
          System.out.println(k);
          done = true;
        }
      }
      k += 2;
    }


  }

  public static boolean isPrime(int n){
    for(int i = 2; i < Math.sqrt(n); i++){
      if(n%i == 0){
        return false;
      }
    }
    return true;
  }
}
