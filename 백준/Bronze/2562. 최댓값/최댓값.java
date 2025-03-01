import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = 1;
        int max = 0;
        int idx = 0;
        while(N <= 9){
            int a = sc.nextInt();
            if(max < a){
                max = a;
                idx = N;
            }
            N++;
        }

        System.out.println(max + "\n" + idx);








    }
}
