import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<Character> sam = new Stack<>();
        for (char c : s.toCharArray()) 
        {
            if (c == '(') 
            {
                sam.push(')');
            }
            else if (c == '{') 
            {
                sam.push('}');
            } 
            else if (c == '[') 
            {
                sam.push(']');
            } 
            else if (sam.isEmpty() || sam.pop() != c)
            {
                return false;
            }
        }
        return sam.isEmpty();
    }
}