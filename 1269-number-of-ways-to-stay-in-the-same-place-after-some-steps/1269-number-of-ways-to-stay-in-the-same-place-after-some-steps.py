class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
            
        n = min(steps//2+1, arrLen)
        l = [0]*(n+2)
        l[1] = 1
        
        for i in range(steps):
            temp = [l[x-1] + l[x] + l[x+1] for x in range(len(l)) if x!=0 and x!=len(l)-1]
            l[1:n+1] = temp
            
        return l[1] % (10**9 + 7)