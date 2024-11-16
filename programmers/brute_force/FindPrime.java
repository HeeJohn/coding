package brute_force;


import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

class FindPrime {
    public int solution(String numbers) {
        Set<Integer> comb = new HashSet<>();

        // 가능한 모든 길이의 숫자 조합 생성
        for (int i = 1; i <= numbers.length(); i++) {
            permuteIterative(numbers, i, comb);
        }

        int counter = 0;

        // 조합된 숫자 중 소수인 숫자를 찾음
        for (Integer c : comb) {
            if (isPrime(c)) {
                System.out.println(c);
                counter++;
            }
        }

        return counter;
    }

    // 재귀 없이 순열을 생성하는 반복적 방식
    private void permuteIterative(String numbers, int length, Set<Integer> comb) {
        Stack<PermutationState> stack = new Stack<>();
        stack.push(new PermutationState("", numbers));

        while (!stack.isEmpty()) {
            PermutationState currentState = stack.pop();
            String prefix = currentState.prefix;
            String remaining = currentState.remaining;

            // 원하는 길이의 조합이 완성되면 comb에 추가
            if (prefix.length() == length) {
                comb.add(Integer.parseInt(prefix));
                continue;
            }

            // 남은 문자열의 각 문자에 대해 조합 생성
            for (int i = 0; i < remaining.length(); i++) {
                String newPrefix = prefix + remaining.charAt(i);
                String newRemaining = remaining.substring(0, i) + remaining.substring(i + 1);
                stack.push(new PermutationState(newPrefix, newRemaining));
            }
        }
    }

    // 소수 판별 함수
    private boolean isPrime(int num) {
        if (num < 2) return false;

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }

        return true;
    }

    // 순열 상태를 저장하는 클래스
    private static class PermutationState {
        String prefix;
        String remaining;

        PermutationState(String prefix, String remaining) {
            this.prefix = prefix;
            this.remaining = remaining;
        }
    }


}


//import java.util.Set;
//import java.util.HashSet;
//import java.util.Stack;
//
//class Solution {
//    public int solution(String numbers){
//        Set<Integer> comp  = new HashSet<>();
//
//        for(int i=1; i<= numbers.length(); i++){
//            permute(comp, i, numbers);
//        }
//
//        int counter = 0;
//
//        for(Integer num : comp){
//            if(isPrime(num)) counter++;
//        }
//
//
//        return counter;
//    }
//
//
//    private void permute(Set<Integer> comp, int length, String numbers){
//        Stack<PermuteState> stack = new Stack<>();
//        stack.push(new PermuteState("", numbers));
//
//        while(!stack.isEmpty()){
//            PermuteState current = stack.pop();
//            String prefix = current.prefix;
//            String remaining = current.remaining;
//
//            if(prefix.length() == length) {
//                comp.add(Integer.parseInt(prefix));
//                continue;
//            }
//
//            for(int i=0;i<remaining.length(); i++){
//
//                PermuteState newState = new PermuteState(
//                        prefix+remaining.charAt(i),
//                        remaining.substring(0,i)+remaining.substring(i+1, remaining.length())
//                );
//
//                stack.push(newState);
//            }
//        }
//
//    }
//
//
//
//    private boolean isPrime(int number){
//        if(number<2) return false;
//
//        for(int i=2 ;i<=Math.sqrt(number); i++){
//            if(number%i ==0) return false;
//        }
//
//        return true;
//    }
//
//}
//
//class PermuteState{
//    String prefix;
//    String remaining;
//
//    PermuteState(String prefix, String remaining){
//        this.prefix = prefix;
//        this.remaining = remaining;
//    }
//}



//import java.util.Set;
//import java.util.HashSet;
//import java.util.Queue;
//import java.util.LinkedList;
//
//class Solution {
//    public int solution(String numbers){
//        Set<Integer> comp  = new HashSet<>();
//
//        for(int i=1; i<= numbers.length(); i++){
//            permute(comp, i, numbers);
//        }
//
//        int counter = 0;
//
//        for(Integer num : comp){
//            if(isPrime(num)) counter++;
//        }
//
//
//        return counter;
//    }
//
//
//    private void permute(Set<Integer> comp, int length, String numbers){
//        Queue<PermuteState> q = new LinkedList<>();
//        q.add(new PermuteState("", numbers));
//
//        while(!q.isEmpty()){
//            PermuteState current = q.poll();
//            String prefix = current.prefix;
//            String remaining = current.remaining;
//
//            if(prefix.length() == length) {
//                comp.add(Integer.parseInt(prefix));
//                continue;
//            }
//
//            for(int i=0;i<remaining.length(); i++){
//
//                PermuteState newState = new PermuteState(
//                        prefix+remaining.charAt(i),
//                        remaining.substring(0,i)+remaining.substring(i+1, remaining.length())
//                );
//
//                q.add(newState);
//            }
//        }
//
//    }
//
//
//
//    private boolean isPrime(int number){
//        if(number<2) return false;
//
//        for(int i=2;i<=Math.sqrt(number); i++){
//            if(number%i ==0) return false;
//        }
//
//        return true;
//    }
//
//}
//
//class PermuteState{
//    String prefix;
//    String remaining;
//
//    PermuteState(String prefix, String remaining){
//        this.prefix = prefix;
//        this.remaining = remaining;
//    }
//}