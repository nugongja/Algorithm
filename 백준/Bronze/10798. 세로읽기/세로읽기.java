import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String[][] arr = new String[5][];
        int maxlen = 0;
        for(int i=0; i<5; i++){
            arr[i] = sc.nextLine().split("");
            if(arr[i].length > maxlen){
                maxlen = arr[i].length;
            }
        }


        String answer = "";
        for(int i=0; i<maxlen; i++){
            for(int j=0; j<5; j++){
                if(arr[j].length > i){
                    answer += arr[j][i];
                }
            }
        }
        System.out.println(answer);




    }
}
