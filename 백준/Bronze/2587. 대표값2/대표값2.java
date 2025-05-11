import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        List<Integer> arr = new ArrayList<>();

        for(int i=0; i<5; i++){
            arr.add(sc.nextInt());
        }

        Collections.sort(arr);

        double agv = arr.stream().mapToInt(Integer::intValue).average().orElse(0);

        System.out.println((int)agv);
        System.out.println(arr.get(2));

    }
}

