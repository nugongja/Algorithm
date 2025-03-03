import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();


        int[] basket = new int[N+1];
        for(int k=1; k<N+1; k++){
            basket[k] = k;
        }

        for(int k=0; k<M; k++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            int tmp = basket[i];
            basket[i] = basket[j];
            basket[j] = tmp;
        }

        for(int k=1; k<N+1; k++){
            System.out.print(basket[k] + " ");
        }





    }
}
