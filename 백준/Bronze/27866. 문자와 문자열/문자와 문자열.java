import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine().trim();
        int i = sc.nextInt() - 1;

        System.out.println(S.charAt(i));


    }
}
