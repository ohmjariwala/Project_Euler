public class Euler4 {
    public static void main(String[] args) {
        int value=0;

        for(int i=100; i<=999; i++){
            for(int j=i; j<=999; j++){
                int value1= i*j;
                StringBuilder sb1= new StringBuilder(""+ value1);
                String sb2= "" + value1;
                sb1.reverse();
                if(sb2.equals(sb1.toString()) && value1>value){
                    value=value1;
                }
            }
        }

        System.out.println(value);

    }
}
