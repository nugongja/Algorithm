import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] baskets = new int[N+1];

        while(M > 0){
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();

            for(int idx=i; idx<j+1; idx++){
                baskets[idx] = k;
            }

            M--;
        }

        for(int i=1; i<baskets.length; i++){
            System.out.print(baskets[i] + " ");
        }





    }
}
