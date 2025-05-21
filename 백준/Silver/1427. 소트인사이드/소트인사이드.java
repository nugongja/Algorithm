import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[][] arr = new int[10][2];
        String s = br.readLine();

        for(int i=0; i<s.length(); i++){
            int tmp = Integer.parseInt(String.valueOf(s.charAt(i)));
            arr[tmp][1] += 1;
        }

        for(int i=9; i>-1; i--){
            bw.append(Integer.toString(i).repeat(arr[i][1]));
        }


        bw.flush();
        bw.close();




    }
}

