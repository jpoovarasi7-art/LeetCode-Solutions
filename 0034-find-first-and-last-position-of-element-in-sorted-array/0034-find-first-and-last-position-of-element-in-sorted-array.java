class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[]{-1, -1};
        
        // Find the first occurrence (left bound)
        result[0] = findBound(nums, target, true);
        
        // If the target isn't present at all, return [-1, -1]
        if (result[0] == -1) {
            return result;
        }
        
        // Find the last occurrence (right bound)
        result[1] = findBound(nums, target, false);
        
        return result;
    }

    private int findBound(int[] nums, int target, boolean isFirst) {
        int left = 0;
        int right = nums.length - 1;
        int bound = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                bound = mid; // Record candidate index
                if (isFirst) {
                    // Keep searching on the left side
                    right = mid - 1;
                } else {
                    // Keep searching on the right side
                    left = mid + 1;
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return bound;
    }
}