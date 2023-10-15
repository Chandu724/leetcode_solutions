class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l = [0]*(n+1)
        if n == 0:
            return 0
        l[1] = 1
        for i in range(2,n+1):
            if i%2==0:
                l[i] = l[i//2]
            else:
                l[i] = l[i//2] + l[i//2 + 1]
                
        return max(l)