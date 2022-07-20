//PE48

public class PE0048{
  public static void main(String[] args){

    long sum = 0L;
    long modulus = 10000000000L;
    for(int i = 1; i <= 1000; i++){
      long temp = i;
      for(int j = 1; j < i; j++){
        temp *= i;
        temp = temp % modulus;
      }

      sum += temp;
      sum = sum % modulus;
    }

    System.out.println(sum);

  }
}
