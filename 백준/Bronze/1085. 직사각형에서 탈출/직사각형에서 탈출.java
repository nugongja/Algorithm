import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();

        // r = 0 or r = w
        // c = 0 or c = h
        int tmp = Math.min(Math.abs(x),Math.abs(y));
        tmp = Math.min(tmp, Math.abs(w-x));
        tmp = Math.min(tmp, Math.abs(h-y));

        System.out.println(tmp);
    }
}
