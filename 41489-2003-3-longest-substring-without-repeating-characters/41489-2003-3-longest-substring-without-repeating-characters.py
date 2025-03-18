class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxc, start = 0, 0
        js = {}
        for i, x in enumerate(s):
            if x in js and js[x] >= start:
                start = js[x] + 1
            else:
                maxc = max(maxc, i-start+1)
            js[x] = i
        
        return maxc
        