import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        String line = sc.nextLine();

        int answer = 0;
        for(int i=0; i<n; i++){
            answer += Integer.parseInt(String.valueOf(line.charAt(i)));

        }
        System.out.println(answer);



    }
}
