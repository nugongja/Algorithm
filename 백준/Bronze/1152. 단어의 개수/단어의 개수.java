import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String line = sc.nextLine().strip();
        if (line.isEmpty()) {
            System.out.println(0);
        } else {
            String[] token = line.split(" ");
            System.out.println(token.length);
        }


    }
}
