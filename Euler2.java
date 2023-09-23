import java.util.ArrayList;
import java.util.List;

public class Euler2 {
    public static void main(String[] args) {
        List <Integer> list= new ArrayList<Integer>();
        int sum=0;
        int limit= 4000000;
        int a=1; int b=2;
        int fib= a+b;
        list.add(a);
        list.add(b);


        while (fib <= limit){
            list.add(fib);
            a=b;
            b=fib;
            fib= a+b;
        }  
        for (int i=0; i< list.size(); i++){
            if (list.get(i)% 2 ==0){
                sum= sum + list.get(i); 
            }
    }
        System.out.println(sum);
        System.out.println(3524578+832040+196418+46368+10946+2584+ 610+ 144+34+8+2);
    }
}
