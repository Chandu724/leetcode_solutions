class Solution:
    def climbStairs(self, n: int) -> int:
        
        x = 1
        y = 2
        
        if n <= 2:
            return n
        
        for i in range(n-2):
            x, y = y, x+y
            
        return y