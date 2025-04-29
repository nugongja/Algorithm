import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        Long n = sc.nextLong();

        Long answer = 0L;
        for(int i=1; i<n-1; i++){
            answer += i*(n-1-i);
        }

        System.out.println(answer);
        System.out.println(3);
    }
}
