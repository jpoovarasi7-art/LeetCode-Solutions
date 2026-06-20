# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            # Prevent potential integer overflow
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is either mid or to its left
                right = mid
            else:
                # If mid is good, the first bad version must be to its right
                left = mid + 1
                
        # When left == right, we have found the first bad version
        return left
