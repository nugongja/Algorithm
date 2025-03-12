import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        String line = sc.nextLine();

        int answer = 1;
        for(int i=0; i<line.length()/2; i++){
            if(line.charAt(i) != line.charAt(line.length()-1-i)){
                answer = 0;
                break;
            }
        }

        System.out.println(answer);


    }
}
