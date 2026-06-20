class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==-2147483648 and divisor ==-1:
            return 2147483647
        is_negative = (dividend <0) != (divisor<0)
        a=abs(dividend)
        b=abs(divisor)
        quotient=0
        while a>=b:
            temp_divisor=b
            multiple=1
            while(a>=(temp_divisor<<1)):
                temp_divisor<<=1
                multiple<<=1
            a-=temp_divisor
            quotient+=multiple
        return -quotient if is_negative else quotient