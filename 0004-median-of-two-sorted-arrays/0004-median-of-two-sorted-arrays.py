class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        ans=list()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i=i+1
            else:
                ans.append(nums2[j])
                j=j+1
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])
        med=len(ans)//2
        if len(ans)%2!=0:
            return float(ans[med])
        else:
            return (ans[med]+ans[med-1])/2.0