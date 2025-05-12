import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int k = sc.nextInt();


        List<Integer> arr = new ArrayList<>();

        for(int i=0; i<N; i++){
            arr.add(-1*sc.nextInt());
        }

        Collections.sort(arr);

        System.out.println(-1*arr.get(k-1));

    }
}

