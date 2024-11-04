package programmers_java.stack;

import java.util.Stack;


class NoSameNum {
    public Stack<Integer> solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();

        stack.push(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            Integer lastEl = stack.pop();
            if (lastEl != arr[i]) stack.push(lastEl);

            stack.push(arr[i]);
        }

        return stack;
    }
}