class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans=0
        a=0
        for i in moves:
            if i=='U':
                ans+=1
            elif i=='D':
                ans-=1
            elif i=='L':
                a+=1
            elif i=='R':
                a-=1
        if ans==0 and a==0:
            return True
        else:
            return False