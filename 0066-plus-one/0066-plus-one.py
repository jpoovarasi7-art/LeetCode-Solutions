class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=""
        result=[]
        for i in range(0,len(digits)):
            str1+=str(digits[i])
        num=int(str1)
        num=num+1
        str2=str(num)
        for i in str2:
            result.append(int(i))
        return result