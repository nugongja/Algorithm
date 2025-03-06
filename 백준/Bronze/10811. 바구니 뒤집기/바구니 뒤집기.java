import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] basket = new int[N];
        for(int i=0; i<N; i++){
            basket[i] = i+1;
        }

        while(M-- > 0){
            int i = sc.nextInt() - 1;
            int j = sc.nextInt() - 1;
            if(i == j) continue;

            for(int k = 0; k<(j-i+1)/2; k++){
                int tmp = basket[i+k];
                basket[i+k] = basket[j-k];
                basket[j-k] = tmp;
            }
        }

        for(int num : basket){
            System.out.print(num + " ");
        }

    }
}
