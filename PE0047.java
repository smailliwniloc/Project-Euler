//PE 47
import java.util.*;

public class PE0047{
  public static void main(String[] args){

    int k = 5;
    while(true){
      ArrayList f1 = new ArrayList();
      ArrayList f2 = new ArrayList();
      ArrayList f3 = new ArrayList();
      ArrayList f4 = new ArrayList();

      factor(k, f1);
      factor(k + 1, f2);
      factor(k + 2, f3);
      factor(k + 3, f4);

      if(f1.size() == 4 && f2.size() == 4 && f3.size() == 4 && f4.size() == 4){
        System.out.println(k);
        break;
      }

      k++;

    }
  }

  public static void factor(int n, ArrayList ar){
    for(int i = 2; i < n/2; i++){
      if(n%i == 0){
        if(!ar.contains(i)){
          ar.add(i);
        }
        if(isPrime(n/i) && i != n/i){
          ar.add(n/i);
          break;
        }
        else{
          factor(n/i, ar);
        }
        break;
      }
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
