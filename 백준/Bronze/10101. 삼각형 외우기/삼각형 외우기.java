import java.io.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if(a == 60 && a == b && a == c){
            System.out.println("Equilateral");
        } else if (a+b+c == 180) {
            if (a != b && b != c && c != a){
                System.out.println("Scalene");
            } else{
                System.out.println("Isosceles");
            }
        } else{
            System.out.println("Error");
        }



    }
}
