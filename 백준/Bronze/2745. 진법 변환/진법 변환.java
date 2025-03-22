import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String[] token = sc.nextLine().split(" ");
        String s = token[0];
        int n = Integer.parseInt(token[1]);


        int sum = 0;
        for(int i=0; i<s.length(); i++){
            int c = s.charAt(i) - '0';

            if(s.charAt(i) >= 'A' && s.charAt(i) <= 'Z'){
                c = s.charAt(i) - 'A' + 10;
            }

            sum += (int) (c*Math.pow(n, s.length()-1-i));
        }

        System.out.println(sum);

    }
}
