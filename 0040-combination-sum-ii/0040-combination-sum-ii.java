import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Sort candidates to group duplicates together and enable early pruning
        Arrays.sort(candidates);
        
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] candidates, int remain, int start) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            // Prune search: if candidate exceeds the remaining target, stop the loop
            if (candidates[i] > remain) {
                break;
            }

            // Skip duplicate elements at the same level of recursion
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            current.add(candidates[i]);
            // Pass 'i + 1' so each element is used at most once
            backtrack(result, current, candidates, remain - candidates[i], i + 1);
            current.remove(current.size() - 1); // Backtrack
        }
    }
}