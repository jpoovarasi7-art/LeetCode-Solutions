import java.util.HashSet;
import java.util.Set;
public class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) {
            first[i] = -1;
            last[i] = -1;
        }
        for (int i = 0; i < s.length(); i++) {
            int curr = s.charAt(i) - 'a';
            if (first[curr] == -1) {
                first[curr] = i;
            }
            last[curr] = i;
        }
        int totalPalindromes = 0;
        for (int i = 0; i < 26; i++) {
            if (first[i] != -1 && first[i] < last[i]) {
                Set<Character> uniqueMiddles = new HashSet<>();
                for (int mid = first[i] + 1; mid < last[i]; mid++) {
                    uniqueMiddles.add(s.charAt(mid));
                }
                totalPalindromes += uniqueMiddles.size();
            }
        }
        return totalPalindromes;
    }
}
