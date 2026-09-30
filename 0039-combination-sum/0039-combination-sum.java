import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] candidates, int remain, int start) {
        if (remain == 0) {
            // Target achieved, save a copy of the valid combination
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            // Skip invalid branch if the candidate exceeds the remaining target
            if (candidates[i] <= remain) {
                current.add(candidates[i]);
                // Pass 'i' instead of 'i + 1' to allow reusing the same element
                backtrack(result, current, candidates, remain - candidates[i], i);
                current.remove(current.size() - 1); // Backtrack
            }
        }
    }
}