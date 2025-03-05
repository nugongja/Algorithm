import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int[] arr = new int[42];

        int count = 10;
        while (count > 0){
            int x = sc.nextInt();
            arr[x%42] += 1;
            count--;
        }

        int answer = (int) Arrays.stream(arr)
                .filter(n -> n>0)
                .count();

        System.out.println(answer);
    }
}
