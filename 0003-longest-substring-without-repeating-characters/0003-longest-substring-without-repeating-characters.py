class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chat=set()
        j=0
        max_length=0
        for i in range(len(s)):
            while s[i] in chat:
                chat.remove(s[j])
                j+=1
            chat.add(s[i])
            max_length=max(max_length,i-j+1)
        return max_length