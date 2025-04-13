import java.io.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[][] land = new int[2][2];
        int N = sc.nextInt();

        while(N > 0){
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(land[0][0] == 0 || x < land[0][0]){
                land[0][0] = x;
            }
            if(land[1][0] == 0 || x > land[1][0]){
                land[1][0] = x;
            }
            if(land[0][1] == 0 || y < land[0][1]){
                land[0][1] = y;
            }
            if(land[1][1] == 0 || y > land[1][1]){
                land[1][1] = y;
            }

            N--;
        }

        System.out.println((land[1][0] - land[0][0])*(land[1][1]-land[0][1]));



    }
}
