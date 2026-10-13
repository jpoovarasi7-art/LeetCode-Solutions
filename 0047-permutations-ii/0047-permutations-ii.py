class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sample=set(itertools.permutations(nums))
        sample1=list(sample)
        return sample1