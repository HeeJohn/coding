package gready;

// 던전 시작 최소 조건 : 1. 최소 필요 피로도
// 던전 마쳤을 때 : 소모 피로도
// 최대한 던전을 많이 탐험하려고 함.

import java.util.Arrays;
import java.util.Stack;

class Energy{

    public int solution(int k, int[][] dungeons){

        return findMaxTraversal(k, dungeons);
    }

    private int findMaxTraversal(int k, int[][] dungeons){
        Stack<EnergyState> stack = new Stack<>();
        stack.push(new EnergyState(k, Arrays.copyOfRange(dungeons, 0, dungeons.length), 0));
        int max = 0;

        while(!stack.isEmpty()){
            EnergyState now = stack.pop();
            int[][] left = now.left;
            int count = now.count;

            if(left.length == 0){
                max = Integer.max(max, count);
                continue;
            }

            for(int i=0;i<left.length;i++){
                int entryEnergy = left[i][0];
                int consumedEnergy = left[i][1];

                if(now.k>= entryEnergy){
                    int[][] temp = new int[left.length-1][2];
                    int[][] one = Arrays.copyOfRange(left, 0, i);
                    int[][] two = Arrays.copyOfRange(left, i+1, left.length);

                    System.arraycopy(one, 0,
                            temp, 0, one.length);
                    System.arraycopy(two, 0,
                            temp, one.length, two.length);

                    stack.push(new EnergyState(
                            now.k-consumedEnergy,
                            temp,
                            count+1
                    ));
                }else{
                    max = Integer.max(max, count);
                }

            }
        }

        return max;
    }

}

class EnergyState{
    int k;
    int[][] left;
    int count;

    EnergyState(int k, int[][] left, int count){
        this.k = k;
        this.count = count;
        this.left= left;
    }
}