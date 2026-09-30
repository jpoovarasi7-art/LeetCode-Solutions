class Solution {
    public int jump(int[] nums) {
        // If array has 1 or 0 elements, no jumps needed
        if (nums == null || nums.length <= 1) {
            return 0;
        }

        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;

        // Iterate through the array (excluding the last element)
        for (int i = 0; i < nums.length - 1; i++) {
            // Update the farthest index reachable from current position
            farthest = Math.max(farthest, i + nums[i]);

            // If we've reached the boundary of the current jump
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest; // Set boundary to farthest point reachable

                // Early exit if we can already reach or pass the last index
                if (currentEnd >= nums.length - 1) {
                    break;
                }
            }
        }

        return jumps;
    }
}