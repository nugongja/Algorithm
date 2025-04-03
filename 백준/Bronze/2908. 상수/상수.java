import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        String[] token = sc.nextLine().split(" ");
        StringBuffer sb = new StringBuffer(token[0]).reverse();
        int tmp1 = Integer.parseInt(sb.toString());
        sb = new StringBuffer(token[1]).reverse();
        int tmp2 = Integer.parseInt(sb.toString());

        if (tmp1 > tmp2){
            System.out.println(tmp1);
        }
        else{
            System.out.println(tmp2);
        }







    }
}
