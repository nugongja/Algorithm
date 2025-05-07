import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine();
        boolean[][] board = new boolean[M][N];

        for(int i=0; i<M; i++){
            String line = sc.nextLine();
            for(int j=0; j<N; j++){
                if(line.charAt(j) == 'W') board[i][j] = true;
                else board[i][j] = false;
            }
        }


        int answer = 51;
        for(int i=0; i<M-8+1; i++) {
            for (int j = 0; j < N-8+1; j++) {
                answer = Math.min(answer, checkBoard(i, j, true, board));
                answer = Math.min(answer, checkBoard(i, j, false, board));
            }
        }

        System.out.println(answer);
    }

    public static int checkBoard(int r, int c, boolean color, boolean[][] board){
        int tmp = 0;
        for(int i=0; i<8; i++){
            for(int j=0; j<8; j++){
                if((i+j)%2 == 0){
                    if(board[r+i][c+j]^color) {
                        tmp += 1;
                    }
                }
                else{
                    if(!board[r+i][c+j]^color){
                        tmp += 1;
                    }
                }
            }
        }
        return tmp;
    }
}

