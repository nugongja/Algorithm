import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] num = new int[N];
        for(int i=0; i<N; i++){
            int X = sc.nextInt();
            num[i] = X;
        }

        int max = Arrays.stream(num).max().getAsInt();
        int min = Arrays.stream(num).min().getAsInt();

        System.out.println(min + " " + max);






    }
}
