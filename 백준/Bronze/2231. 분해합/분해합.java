import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int answer = 0;

        for(int i=1; i<N; i++){
            int tmp = i;
            for(int j=0; j<Integer.toString(i).length(); j++){
                tmp += Integer.parseInt(String.valueOf(Integer.toString(i).charAt(j)));
            }
            if(tmp == N){
                answer = i;
                break;
            }
        }

        System.out.println(answer);

    }
}
