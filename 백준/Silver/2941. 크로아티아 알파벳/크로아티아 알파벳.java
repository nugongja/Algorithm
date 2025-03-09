import java.io.*;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();


        String regex = "dz=|lj|nj|c=|c-|d-|s=|z=";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);

        int count = 0;
        while (matcher.find()){
            count++;
        }

        int answer = count + line.replaceAll(regex, "").length();
        System.out.println(answer);
    }


}
