package programmers_java.sort;

import java.util.Arrays;

class KthNumber{
    public int[] solution(int[]array, int[][] commands){
        int[] answer = new int[commands.length];

        for(int i =0; i< commands.length ;i++){
            int[] tempArray = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(tempArray);
            answer[i]= tempArray[commands[i][2]-1];
        }

        return answer;
    }
}
