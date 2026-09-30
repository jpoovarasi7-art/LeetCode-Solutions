import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        // Early exit: odd length strings can never be valid
        if (s.length() % 2 != 0) {
            return false;
        }

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // Push expected closing bracket onto the stack
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else {
                // If stack is empty or top element doesn't match current closing bracket
                if (stack.isEmpty() || stack.pop() != c) {
                    return false;
                }
            }
        }

        // Return true if all opening brackets were properly closed
        return stack.isEmpty();
    }
}