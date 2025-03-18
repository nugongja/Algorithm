import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;

        while((line = br.readLine()) != null){
            sb.append(line).append("\n");
        }

        System.out.println(sb.toString());
    }
}
