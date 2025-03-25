import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int answer = (int) ((Math.pow(2,N)+1)*(Math.pow(2,N)+1));
        System.out.println(answer);





    }
}