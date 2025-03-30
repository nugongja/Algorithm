import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        double a;
        double b;
        while(((a = sc.nextDouble()) != 0) && ((b = sc.nextDouble()) != 0)) {
            if(a < b && (b/a) - (int)(b/a) == 0){
                System.out.println("factor");
            }
            else if(a > b && (a/b) - (int)(a/b) == 0){
                System.out.println("multiple");
            }
            else{
                System.out.println("neither");
            }
        }
    }
}
