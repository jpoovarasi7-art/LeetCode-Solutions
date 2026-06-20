class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d1=int(a,2)
        d2=int(b,2)
        ans=d1+d2
        return bin(ans)[2:]