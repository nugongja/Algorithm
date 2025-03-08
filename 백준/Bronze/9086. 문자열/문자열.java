import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t > 0){
            String s = sc.next().trim();
            System.out.println(s.charAt(0) +"" + s.charAt(s.length()-1));
            t--;
        }


    }
}
