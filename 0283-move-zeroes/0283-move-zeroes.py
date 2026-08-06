class Solution(object):
    def moveZeroes(self, nums):
        k = 0  # index for non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
                
                
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        