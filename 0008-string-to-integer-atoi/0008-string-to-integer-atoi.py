class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        res = 0
        
        # 32-bit signed integer limits
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        # Step 2: Handle sign character
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
            
        # Step 3: Convert valid digit characters
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Step 4: Overflow check before updating res
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            index += 1
            
        return sign * res
