class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        int x2 = (int) ((brown/2 - 2) + Math.sqrt(Math.pow(brown/2 - 2, 2)-4*yellow))/2;
        int y2 = yellow/x2;

        answer = new int[] { x2+2, y2+2 };

        
        return answer;
    }
}