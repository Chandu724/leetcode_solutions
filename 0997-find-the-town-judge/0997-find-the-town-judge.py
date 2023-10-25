class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        a = [i[0] for i in trust]
        b = [i[1] for i in trust]
        
        if len(set(a)) != n-1:
            return -1
        
        for i in range(1,n+1):
            if b.count(i) == n-1 and i not in a:
                return i
            
        return -1