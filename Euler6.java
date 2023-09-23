import java.util.stream.IntStream;

public class Euler6 {


    public static void main(String[] args) {

        int sumA=0;
        int sumB=0;
        int[] a = IntStream.range(1, 101).toArray(); //sum of squares
        int[] b = IntStream.range(1, 101).toArray(); //square of sums

    


        for(int i=1; i<a.length+1; i++){
            sumA += (i*i);
        }

        for (int i=1; i<b.length+1; i++){
            sumB += i;
        }

        int sumBSquared= (int) Math.pow(sumB, 2);


        System.out.println(sumBSquared- sumA);
    }
}
