import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        number = [str(i) for i in range(1,n+1)]
        result=[]
        k-=1
        fact=math.factorial(n-1)
        for i in range(n-1,0,-1):
            idx=k//fact
            result.append(number.pop(idx))
            k%=fact
            fact=fact//i

        result.append(number[0])
        return "".join(result)    