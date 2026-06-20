class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        count = {}
        for num in nums1:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        for num in nums2:
            if num in count and count[num]>0:
                ans.append(num)
                count[num] -= 1
        return ans