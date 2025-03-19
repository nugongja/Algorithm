import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String S = sc.nextLine();
        int[] alp = new int[26];
        for(int i=0; i<26; i++){
            alp[i] = -1;
        }

        for(int i=0; i<S.length(); i++){
            char c = S.charAt(i);
            int idx = Character.getNumericValue(c) - 10;
            if(alp[idx] == -1){
                alp[idx] = i;
            }
        }

        for(int i : alp){
            System.out.print(i + " ");
        }
    }
}
