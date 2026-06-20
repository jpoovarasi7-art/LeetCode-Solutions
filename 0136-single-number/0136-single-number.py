class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)    
        """
        :type nums: List[int]
        :rtype: int
        """
        