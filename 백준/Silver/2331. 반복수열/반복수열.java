import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int P = sc.nextInt();

        List<Integer> D = new ArrayList<>();
        D.add(-1);
        D.add(A);

        int idx = 2;
        while(true){
            String s = Integer.toString(D.get(idx-1));
            int tmp = 0;
            for(int i=0; i<s.length();i++){
                tmp += (int)Math.pow(Character.getNumericValue(s.charAt(i)), P);
            }
            if(D.contains(tmp)){
                int k = D.indexOf(tmp);
                D = new ArrayList<>(D.subList(0, k));
                break;
            }
            D.add(tmp);
            idx++;
        }

        System.out.println(D.size() - 1);
    }
}
