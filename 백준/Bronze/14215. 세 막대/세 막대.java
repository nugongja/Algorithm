import java.io.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if(a==b && b==c) {
            System.out.println(a+b+c);
        } else {
            if (a >= b+c) {
                System.out.println(2*(b+c)-1);
            } else if (b >= a+c){
                System.out.println(2*(a+c)-1);
            } else if(c >= a+b){
                System.out.println(2*(b+a)-1);
            } else{
                System.out.println(a+b+c);
            }
        }


    }
}
