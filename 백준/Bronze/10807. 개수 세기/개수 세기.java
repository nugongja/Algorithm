import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[] tokens = br.readLine().split(" ");
        int v = Integer.parseInt(br.readLine());
        int answer = 0;

        for(int i=0; i<tokens.length; i++){
            int num = Integer.parseInt(tokens[i]);
            if(num == v){
                answer++;
            }
        }
        System.out.println(answer);

    }
}
