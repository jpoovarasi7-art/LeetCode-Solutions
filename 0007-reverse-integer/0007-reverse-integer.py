class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        x = abs(x)
        reverse_s = int(str(x)[::-1])*sign
        if reverse_s<-2**31 or reverse_s>2**31-1:
            return 0
        return reverse_s