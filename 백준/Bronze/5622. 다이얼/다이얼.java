import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        Map<Character, Integer> charToNumber = new HashMap<>();

        String[] alp = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        int[] numbers = {2,3,4,5,6,7,8,9};

        for (int i = 0; i < alp.length; i++) {
            for (char c : alp[i].toCharArray()) {
                charToNumber.put(c, numbers[i]);
            }
        }

        String line = sc.nextLine();

        int answer = 0;
        for(int i=0; i<line.length(); i++){
            int next_idx = charToNumber.get(line.charAt(i));
            answer += 1 + next_idx;
        }

        System.out.println(answer);


    }
}
