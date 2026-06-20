class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if sorted(s1[0::2])!=sorted(s2[0::2]):
            return False
        if sorted(s1[1::2])!=sorted(s2[1::2]):
            return False
        return True