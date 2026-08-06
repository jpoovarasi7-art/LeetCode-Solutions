class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1/x
            n=-n
        i=1
        value=x
        while n>0:
            if n%2==1:
                i*=value
            value*=value
            n=n//2
        return i