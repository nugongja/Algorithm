import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();

        int level = 1;
        int range = 1;
        while(X > range){
            level++;
            range += level;
        }

        int row = 1;
        int col = 1;
        int tmp = 1;
        if(level%2 == 0){       // 짝수는 오른쪽 위에서 왼쪽 아래로
            row = 1;
            col = level;
            tmp = range-level+1;
            while(tmp < X){
                row += 1;
                col -= 1;
                tmp += 1;
            }
        }
        else{                   // 홀수는 왼쪽 아래에서 오른쪽 위로
            row = level;
            col = 1;
            tmp = range-level+1;
            while(tmp < X){
                row -= 1;
                col += 1;
                tmp += 1;
            }
        }

        System.out.println(row + "/" + col);



    }
}
