# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        res = [i for i in range(n)]

        print(res)
        for i in range(n):
            j=0
            while j < len(res):
                if not knows(i, res[j]):
                    res.pop(j)
                else:
                    j = j + 1
                    
        print("\n",res)
                    
        
        if len(res) == 1:
            x = res[0]
            for i in range(n):
                if knows(x, i) and x != i:
                    return -1
            return x
        else:
            return -1