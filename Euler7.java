public class Prime {
    //What is the 10 001st prime number?

    public static boolean is_Prime(int n){
        if (n<2){
            return false;
        }
        int i=2;
        while (i*i <=n){
            if (n %i ==0){
                return false;
            }
            i++;
        }
        return true;
    }

    public static int n_Prime(int n){
        int j=2;
        while (n>0){
            if (is_Prime(j)){
                n--;
                if (n==0){
                    return j;
                }
            }
            j ++;
        }
        return -1;
    }
    public static void main(String[] args) {
        System.out.println(n_Prime(6));
    }
}
