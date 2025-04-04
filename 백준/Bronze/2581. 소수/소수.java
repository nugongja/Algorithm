import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        boolean[] isNotPrime = new boolean[10001];

        int M = sc.nextInt();
        int N = sc.nextInt();

        isNotPrime[0] = true;
        isNotPrime[1] = true;


        for(int i=2; i<10001; i++){
            if(!isNotPrime[i]){
                for(int j=i+i; j<10001; j+=i){
                    isNotPrime[j] = true;
                }
            }
        }

        int sum = 0;
        int min_value = -1;
        for(int i=M; i<N+1; i++){
            if(!isNotPrime[i]){
                sum += i;
                if(min_value < 0){
                    min_value = i;
                }
            }
        }

        if(min_value < 0){
            System.out.println(min_value);
        }
        else {
            System.out.println(sum);
            System.out.println(min_value);
        }






    }
}
