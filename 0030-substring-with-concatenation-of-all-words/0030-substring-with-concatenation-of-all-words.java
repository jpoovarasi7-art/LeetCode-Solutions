import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int wordCount = words.length;
        int totalLen = wordLen * wordCount;

        if (s.length() < totalLen) {
            return result;
        }

        // Frequency map of expected words
        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        // Run sliding window for each offset up to wordLen
        for (int i = 0; i < wordLen; i++) {
            int left = i;
            int right = i;
            int count = 0;
            Map<String, Integer> currentMap = new HashMap<>();

            while (right + wordLen <= s.length()) {
                String word = s.substring(right, right + wordLen);
                right += wordLen;

                if (wordMap.containsKey(word)) {
                    currentMap.put(word, currentMap.getOrDefault(word, 0) + 1);
                    count++;

                    // If a word appears more times than required, shrink window from left
                    while (currentMap.get(word) > wordMap.get(word)) {
                        String leftWord = s.substring(left, left + wordLen);
                        currentMap.put(leftWord, currentMap.get(leftWord) - 1);
                        count--;
                        left += wordLen;
                    }

                    // If all words match, store starting index
                    if (count == wordCount) {
                        result.add(left);
                    }
                } else {
                    // Invalid word reset window state
                    currentMap.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return result;
    }
}