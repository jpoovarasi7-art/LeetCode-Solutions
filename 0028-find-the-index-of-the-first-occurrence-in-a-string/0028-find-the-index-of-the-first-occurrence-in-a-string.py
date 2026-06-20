class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: Empty needle always returns 0
        if not needle:
            return 0
            
        n, m = len(haystack), len(needle)
        
        # Slide a window of length m over haystack
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
                
        return -1
