class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        l = range(n+1)
        x=n
        while x > 0:
            if x&(x-1) == 0:
                res = [res[i]+1 if l[i] >= x else res[i] for i in range(n+1)]
                l = [l[i]-x if l[i] >= x else l[i] for i in range(n+1)]
                x = x//2
            else:
                x-=1
                
        return res