import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int[][] arr = new int[10001][2];

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            int tmp = Integer.parseInt(br.readLine());
            arr[tmp][1] += 1;
        }

        for(int i=0; i<10001; i++){
            for(int j=0; j<arr[i][1]; j++){
                bw.append(Integer.toString(i));
                bw.append("\n");
            }
        }

        bw.flush();
        bw.close();




    }
}

