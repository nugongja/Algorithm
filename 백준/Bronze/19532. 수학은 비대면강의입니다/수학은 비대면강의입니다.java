import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int f = sc.nextInt();

        int x; int y;

        if (a*e-d*b == 0){
            y = (c*d-a*f)/(b*d-a*e);
            if(a==0){
                x = (f-e*y)/d;
            } else{
                x = (c-b*y)/a;
            }

        }
        else{
            x = (c*e-f*b)/(a*e-d*b);
            if(b == 0){
                y = (f-d*x)/e;
            } else{
                y = (c-a*x)/b;
            }
        }

        System.out.println(x + " " + y);
    }
}
