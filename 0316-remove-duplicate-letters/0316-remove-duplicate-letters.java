import java.util.Stack;
public class Solution {
    public static String removeDuplicateLetters(String s) {
        int[] remainingCount = new int[26];
        for (int i = 0; i < s.length(); i++) {
            remainingCount[s.charAt(i) - 'a']++;
        }
        Stack<Character> stack = new Stack<>();
        boolean[] visited = new boolean[26]; 
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            remainingCount[ch - 'a']--; 
            if (visited[ch - 'a']) {
                continue;
            }
            while (!stack.isEmpty() && ch < stack.peek() && remainingCount[stack.peek() - 'a'] > 0) {
                char removedChar = stack.pop();
                visited[removedChar - 'a'] = false;
            }
            stack.push(ch);
            visited[ch - 'a'] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : stack) {
            sb.append(ch);
        }

        return sb.toString();
    }
    public static void main(String[] args) {
        System.out.println(removeDuplicateLetters("bcabc"));    
        System.out.println(removeDuplicateLetters("cbacdcbc")); 
    }
}