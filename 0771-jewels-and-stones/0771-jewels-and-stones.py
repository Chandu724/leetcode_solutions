class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js = {}
        for i in stones:
            if i not in js:
                js[i] = 1
            else:
                js[i] = js[i] + 1
                
        s = 0
        for i in jewels:
            if i in stones:
                s = s + js[i]
            
        return s