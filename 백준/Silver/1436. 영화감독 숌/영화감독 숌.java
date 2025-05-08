import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int cnt = 0;
        for(int i=666; i<6665001; i++){
            String tmp = Integer.toString(i);
            if(tmp.contains("666")){
                cnt += 1;
            }
            if(cnt == n){
                System.out.println(tmp);
                break;
            }
        }




    }


}

