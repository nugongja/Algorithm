import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        while(n > 0){
            int[] alp = new int[26];
            for(int i=0; i< 26; i++){
                alp[i] = -1;
            }

            String s = sc.next().trim();
            for(int i=0; i<s.length(); i++){
                int idx = s.charAt(i) - 97;
                if(alp[idx] == -1 || i-alp[idx] == 1){
                    alp[idx] = i;
                }
                else{
                    break;
                }
                if(i == s.length()-1) {
                    answer +=1;
                }
            }
            n--;
        }
        System.out.println(answer);


    }
}
