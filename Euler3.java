public class Euler3 {
    public static void main(String[] args) {
        long a= 600851475143L;
        long largestPrimeFactor= 1;

        // <= sign is crucial
        for (long i=2; i<= a; i++){
            while (a % i ==0){
               largestPrimeFactor = i;
               a /= i;
            }
        }
        System.out.println(largestPrimeFactor);
    //600851475143

    }
}
