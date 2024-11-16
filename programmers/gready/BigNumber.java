package gready;


import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

class BigNumber {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < number.length(); i++) {
            char current = number.charAt(i);

            while (!stack.isEmpty() && stack.peek() < current && k > 0) {
                stack.pop();
                k--;
            }

            stack.push(current);
        }

        while (k > 0) {
            stack.pop();
            k--;
        }
        Deque<Integer > dq = new LinkedList<>();
        
        StringBuilder answer = new StringBuilder();
        for (char c : stack) {
            answer.append(c);
        }

        return answer.toString();
    }
}
