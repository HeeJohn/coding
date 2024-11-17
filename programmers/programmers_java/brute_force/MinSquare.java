package programmers_java.brute_force;

class MinSquare{
    public int solution(int[][] size){
        int w = Integer.MIN_VALUE;
        int h = Integer.MIN_VALUE;

        for(int[] square : size){

            if(square[0] < square[1]){
                w = Integer.max(w, square[1]);
                h = Integer.max(h, square[0]);
            }else{
                w = Integer.max(w, square[0]);
                h = Integer.max(h, square[1]);
            }
        }

        return w*h;
    }
}