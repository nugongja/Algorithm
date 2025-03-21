import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        while(T > 0) {
            String[] token = sc.nextLine().split(" ");
            int R = Integer.parseInt(token[0]);
            String S = token[1];
            String P = "";
            for (int i = 0; i < S.length(); i++) {
                P += Character.toString(S.charAt(i)).repeat(R);
            }
            System.out.println(P);
            T--;
        }

    }
}
