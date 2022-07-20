//PE45

import java.util.*;

public class PE0045{
  public static void main(String[] args){

    boolean done = false;
    int i = 144;
    while(!done){
      long num = i * (2*i - 1);

      if(isPent(num)){
        System.out.println(num);
        done = true;
      }

      i++;


    }


  }

  public static boolean isPent(long k){
    double num = (0.5 + Math.sqrt(0.25 + 6*k))/3.0;
    return (num == (int)num);
  }
}
