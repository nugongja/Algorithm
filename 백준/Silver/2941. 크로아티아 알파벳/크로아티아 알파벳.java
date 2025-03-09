import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        int answer = 0;
        int len = line.length();
        while(true){
            if(line.contains("dz=")){
                line = line.replaceAll("dz=", " ");
                answer += (len - line.length())/2;
                len = line.length();
            }
            if(line.contains("lj")){
                line = line.replaceAll("lj", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("nj")){
                line = line.replaceAll("nj", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("c=")){
                line = line.replaceAll("c=", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("c-")){
                line = line.replaceAll("c-", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("d-")){
                line = line.replaceAll("d-", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("s=")){
                line = line.replaceAll("s=", " ");
                answer += (len - line.length());
                len = line.length();
            }
            if(line.contains("z=")){
                line = line.replaceAll("z=", " ");
                answer += (len - line.length());
                len = line.length();
            }
            else{
                line = line.replaceAll(" ", "");
                answer += line.length();
                break;
            }
        }
        System.out.println(answer);
    }


}
