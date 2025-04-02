import java.io.*;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        boolean[] isNotPrime = new boolean[1001];

        isNotPrime[0] = true;
        isNotPrime[1] = true;
        for(int i=2; i<1001; i++){
            if(!isNotPrime[i]){
                for(int j=i+i; j<1001; j+=i){
                    isNotPrime[j] = true;
                }
            }
        }



        int answer = 0;
        while(N>0){
            int a = sc.nextInt();
            if(!isNotPrime[a]){
                answer += 1;
            }
            N--;
        }

        System.out.println(answer);




    }
}
