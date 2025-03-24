import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        while(T>0){

            int C = sc.nextInt();
            int Quarter = (int)(C/25);
            int Dime = (int)((C%25)/10);
            int Nickel = (int)(((C%25)%10))/5;
            int Penny = (int)((int)(((C%25)%10))%5);

            System.out.println(Quarter + " " + Dime + " " + Nickel + " " + Penny);
            T--;
        }



    }
}
