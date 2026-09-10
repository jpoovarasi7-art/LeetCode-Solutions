import java.util.Stack;
class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int currentResult = 0;
        int currentNumber = 0;
        int sign = 1; 
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                currentNumber = currentNumber * 10 + (ch - '0');
            } else if (ch == '+') {
                currentResult += sign * currentNumber;
                currentNumber = 0;
                sign = 1;
            } else if (ch == '-') {
                currentResult += sign * currentNumber;
                currentNumber = 0;
                sign = -1;
            } else if (ch == '(') {
                stack.push(currentResult);
                stack.push(sign);
                currentResult = 0;
                sign = 1;
            } else if (ch == ')') {
                currentResult += sign * currentNumber;
                currentNumber = 0;
                currentResult *= stack.pop(); 
                currentResult += stack.pop();
            }
        }
        if (currentNumber != 0) {
            currentResult += sign * currentNumber;
        }
        return currentResult;
    }
}