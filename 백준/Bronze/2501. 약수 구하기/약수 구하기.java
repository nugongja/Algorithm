import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();


        int answer = 0;
        int cnt = 0;
        for(int i=1; i<Math.sqrt(N); i++){
            if(N%i == 0){
                cnt += 2;
            }
        }

        if(Math.sqrt(N) - (int)Math.sqrt(N) == 0){
            cnt += 1;
        }


        int idx = 1;
        for(int i=1; i<(int)Math.sqrt(N)+1; i++){
            if(N%i == 0){
                if(idx == K){
                    answer = i;
                    break;
                }
                else if(cnt + 1 - idx == K){
                    answer = N/i;
                    break;
                }
                idx += 1;
            }
        }

        System.out.println(answer);
    }
}
