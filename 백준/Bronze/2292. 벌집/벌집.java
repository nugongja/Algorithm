import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int cnt = 1;
        int range = 1;

        while(N > range){
            range += 6*cnt;
            cnt++;
        }

        System.out.println(cnt);


    }
}
