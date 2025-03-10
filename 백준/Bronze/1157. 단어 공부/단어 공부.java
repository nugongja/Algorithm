import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        String line = sc.nextLine().toUpperCase();
        int[] alp = new int[26];

        for(int i=0; i<line.length(); i++){
            alp[line.charAt(i)-65]++;
        }

        int cnt = Arrays.stream(alp).max().getAsInt();
        if(Arrays.stream(alp).filter(n->n==cnt).count() > 1){
            System.out.println("?");
        }
        else{
            for(int i=0; i<26; i++){
                if(alp[i] == cnt){
                    System.out.println(Character.toChars(i+65));
                }
            }
        }
    }


}
