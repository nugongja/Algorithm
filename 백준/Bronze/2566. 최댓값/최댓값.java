import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[9][9];

        int tmp = -1;
        int r = -1;
        int c = -1;
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                arr[i][j] = sc.nextInt();
                if(arr[i][j] > tmp){
                    tmp = arr[i][j];
                    r = i;
                    c = j;
                }
            }
        }

        System.out.println(tmp);
        System.out.println((r+1) + " " + (c+1));

    }
}
