import itertools
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letter=['a','b','c']
        happy=[]
        result=list(itertools.product(letter,repeat=n))
        for p in result:
            is_happy=True
            for i in range(n-1):
                if p[i]==p[i+1]:
                    is_happy=False
                    break
            if is_happy:
                happy.append("".join(p))
        return happy[k-1] if k <=len(happy) else ""