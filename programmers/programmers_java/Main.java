package programmers_java;

import programmers_java.sort.Hindex;

class Main{
    public static void main(String[] args) {
        Hindex index = new Hindex();

        int result = index.solution(new int[]{0,0,0,0,0});
        System.out.println(result);

        int result2 = index.solution(new int[]{0,1,1,1,2,2,3,3,5});
        System.out.println(result2);

    }
}