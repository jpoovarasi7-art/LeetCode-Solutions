class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: Empty input list
        if not strs:
            return ""
            
        # Initialize prefix with the first string
        prefix = strs[0]
        
        # Compare prefix against all other strings
        for i in range(1, len(strs)):
            # Keep shrinking the prefix until it matches the start of strs[i]
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                # If prefix shrinks to empty, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix
