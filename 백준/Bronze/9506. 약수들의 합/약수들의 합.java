import java.io.*;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int n;
        while((n=sc.nextInt()) != -1){
            int[] arr = new int[n];

            arr[1] = 1;
            for(int i=2; i<Math.sqrt(n)+1; i++){
                if(n%i == 0){
                    arr[i] = 1;
                    arr[n/i] = 1;
                }
            }

            int sum = IntStream.range(0,n)
                    .filter(i -> arr[i] == 1)
                    .sum();

            if(sum == n){
                StringBuilder sb = new StringBuilder();
                sb.append(n).append(" = ");
                for(int i=1; i<n; i++){
                    if(arr[i] == 1) {
                        sb.append(i).append(" + ");
                    }
                }
                sb.delete(sb.length()-3, sb.length()-1);
                System.out.println(sb);
            }
            else{
                System.out.println(n + " is NOT perfect.");
            }
        }

    }
}
