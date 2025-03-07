import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        double[] score = new double[N];

        int i = 0;
        while(i < N){
            score[i] = sc.nextInt();
            i++;
        }

        Arrays.sort(score);

        double M = Arrays.stream(score).max().getAsDouble();

        double sum = 0;
        for(i=0; i<N; i++){
            sum += ((score[i]*100)/M);
        }

        System.out.println(sum/N);






    }
}
