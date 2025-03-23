import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int B = sc.nextInt();
        StringBuilder answer = new StringBuilder();

        while(N > 0){
            int c = N%B;
            if(c >= 10){
                answer.append((char)(c+55));
            }
            else{
                answer.append((char)(c+48));
            }

            N /= B;
        }

        System.out.println(answer.reverse().toString());



    }
}
