import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double V = sc.nextDouble();

        double answer = (V-A)/(A-B);

        if (answer - (int)answer > 0){
            answer += 1;
        }

        System.out.println((int)answer + 1);

    }
}
