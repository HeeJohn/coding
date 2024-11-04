package programmers_java.stack;


import java.util.Stack;

//
class ProperParenthesis {
    public boolean solution(String s) {
        Stack<Character> cStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                cStack.push(c);
            } else {
                if (cStack.isEmpty()) return false;
                cStack.pop();
            }
        }

        return cStack.size() == 0;
    }
}