import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int tmp = 2;
        while(N > 1){
            if(N%tmp == 0){
                System.out.println(tmp);
                N /= tmp;
            }
            else{
                tmp += 1;
            }
        }


    }
}
