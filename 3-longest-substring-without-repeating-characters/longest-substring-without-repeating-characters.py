class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxc = 0
        js = {}
        for i, x in enumerate(s):
            if x in js:
                z = js[x]
                maxc = max(maxc, len(js))
                for j in list(js.keys()):
                    if js[j] <= z:
                        js.pop(j)
                js[x] = i
            else:
                js[x] = i
        
        return max(maxc, len(js))
        