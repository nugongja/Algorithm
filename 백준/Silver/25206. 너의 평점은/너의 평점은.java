import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        double sum_score = 0;
        double sum = 0;

        int N = 20;
        while(N-- > 0){
            String[] line = sc.nextLine().split(" ");
            if(line[2].equals("P")) {
                continue;
            }
            sum += Double.parseDouble(line[1]);
            sum_score += getScore(Double.parseDouble(line[1]), line[2]);
        }
        System.out.println(sum_score/sum);

    }

    private static double getScore(double score, String grade){
        switch (grade){
            case "A+": return score*4.5;
            case "A0": return score*4.0;
            case "B+": return score*3.5;
            case "B0": return score*3.0;
            case "C+": return score*2.5;
            case "C0": return score*2.0;
            case "D+": return score*1.5;
            case "D0": return score*1.0;
            default: return 0.0;
        }
    }
}
