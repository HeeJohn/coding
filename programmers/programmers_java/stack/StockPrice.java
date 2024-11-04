package programmers_java.stack;
// input : 초 단위로 기록된 주식 가격 배옇
// output : 가격이 떨어지지 않은 기간 : 몇초

import java.util.Stack;

class StockPrice {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();


        for (int i = 0; i < prices.length; i++) {
            int currentPrice = prices[i];

            // 스택이 비어 있지 않고, 스택의 마지막 요소가 현재 가격보다 클 때
            while (!stack.isEmpty() && prices[stack.peek()] > currentPrice) {
                int timeIndex = stack.pop();
                answer[timeIndex] = i - timeIndex;
            }

            stack.push(i);
        }

        // 남아 있는 스택 요소에 대해 가격이 떨어지지 않은 기간 계산
        int maxSec = prices.length - 1;
        while (!stack.isEmpty()) {
            int timeIndex = stack.pop();
            answer[timeIndex] = maxSec - timeIndex;
        }

        return answer;
    }
}
