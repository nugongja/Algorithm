import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        int n = sc.nextInt();
        sc.nextLine();
        int[][] arr = new int[101][101];

        while(n > 0){
            int a = sc.nextInt();
            int b = sc.nextInt();
            for(int i=a; i<a+10; i++){
                for(int j=b; j<b+10; j++){
                    arr[i][j] = 1;
                }
            }
            n--;
        }

        int answer = 0;
        for(int i=1; i<101; i++){
            for(int j=1; j<101; j++){
                answer += arr[i][j];
            }
        }

        System.out.println(answer);
    }
}
