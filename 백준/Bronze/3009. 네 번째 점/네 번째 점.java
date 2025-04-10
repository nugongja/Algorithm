import java.io.*;
import java.util.HashMap;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        HashMap<Integer, Integer> X = new HashMap<>();
        HashMap<Integer, Integer> Y = new HashMap<>();

        for(int i=0; i<3; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            X.put(x, X.getOrDefault(x, 0) + 1);
            Y.put(y, Y.getOrDefault(y, 0)+1);
        }

        X.entrySet().stream()
                .filter(entry -> entry.getValue() == 1)
                .forEach(entry -> System.out.print(entry.getKey() + " "));

        Y.entrySet().stream()
                .filter(entry -> entry.getValue() == 1)
                .forEach(entry -> System.out.print(entry.getKey()));

    }
}
