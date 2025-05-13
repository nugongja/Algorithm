import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 출력은 BufferedWriter 사용
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> arr = new PriorityQueue<>();

        for(int i=0; i<N; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }

        while(!arr.isEmpty()){
            bw.append(arr.poll()+ "\n");
        }

        bw.flush(); // 버퍼에 남은 데이터 출력
        bw.close();
        br.close();

    }
}

