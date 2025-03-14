import java.io.*;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();


        int[][] A = new int[N][M];
        int[][] B = new int[N][M];

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                A[i][j] = sc.nextInt();
            }
        }

        int[][] res = new int[N][M];
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                B[i][j] = sc.nextInt();
                res[i][j] = A[i][j] + B[i][j];
            }
        }


        IntStream.range(0, N).forEach(i -> {
            IntStream.range(0, M).forEach(j -> System.out.print(res[i][j] + " "));
            System.out.println();
        });





    }
}
