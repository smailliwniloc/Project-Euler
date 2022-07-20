//PE49

import java.util.*;

public class PE0049{
  public static void main(String[] args){

    ArrayList<Integer> primes = new ArrayList();

    for(int i = 1001; i < 10000; i+=2){
      if(isPrime(i)){
        primes.add(i);
      }
    }

    for(int i = 0; i < primes.size(); i++){
      for(int j = i+1; j < primes.size(); j++){
        Integer k = primes.get(j) + (primes.get(j) - primes.get(i));
        if(isPrime(k)){
          int x = primes.get(i);
          int y = primes.get(j);
          int z = k;
          if(isPerm(x,y) && isPerm(x,z)){
            System.out.println(x);
            System.out.println(y);
            System.out.println(z);
            break;
          }

        }
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

  public static boolean isPerm(int i, int j){
    char[] cai = String.valueOf(i).toCharArray();
    char[] caj = String.valueOf(j).toCharArray();
    Arrays.sort(cai);
    Arrays.sort(caj);

    String si = "";
    String sj = "";

    for(int a = 0; a < cai.length; a++){
      si += cai[a];
      sj += caj[a];
    }

    if(si.equals(sj)){
      return true;
    }
    else{
      return false;
    }
  }
}
