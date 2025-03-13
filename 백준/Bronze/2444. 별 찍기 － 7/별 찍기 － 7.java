import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=0; i<N; i++){
            System.out.println(" ".repeat(N-1-i) + "*".repeat(2*i+1));
        }

        for(int i=N-2; i>-1; i--){
            System.out.println(" ".repeat(N-1-i) + "*".repeat(2*i+1));
        }


    }
}
