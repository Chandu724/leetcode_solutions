class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        res = []
        for i in range(100, 999, 2):
            cc = Counter(digits)
            a = i//100
            b = (i%100)//10
            c = i%10
            
            if cc[a] > 0:
                cc[a] -= 1
                if cc[b] > 0:
                    cc[b] -=1
                    if cc[c] > 0:
                        res.append(i)
                        
        return res
            
            