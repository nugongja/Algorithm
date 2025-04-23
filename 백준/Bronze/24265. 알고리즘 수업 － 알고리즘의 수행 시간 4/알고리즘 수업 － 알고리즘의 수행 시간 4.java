import java.io.*;
import java.util.Scanner;
import java.util.stream.LongStream;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        Long n = sc.nextLong();

        System.out.println(LongStream.range(1,n).sum());
        System.out.println(2);
    }
}
