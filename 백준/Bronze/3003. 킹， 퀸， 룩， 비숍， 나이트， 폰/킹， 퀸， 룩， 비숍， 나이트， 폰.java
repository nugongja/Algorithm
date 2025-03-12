import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int[] num = {1, 1, 2, 2, 2, 8};

        int[] arr = Arrays.stream(sc.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] res = IntStream.range(0, num.length)
                .map(i -> num[i] - arr[i])
                .toArray();

        for(int k : res){
            System.out.print(k + " ");
        }








    }
}
