class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Pointer to place elements not equal to val

        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val, keep it
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
}