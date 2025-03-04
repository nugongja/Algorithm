import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int N = 28;
        int[] student = new int[31];
        while(N > 0){
            student[sc.nextInt()] = 1;
            N--;
        }

        for(int i=1; i<31; i++){
            if(student[i] == 0){
                System.out.println(i);
            }
        }
    }
}
