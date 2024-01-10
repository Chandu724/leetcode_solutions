class Solution:
    def minTimeToType(self, word: str) -> int:
        s = len(word)
        word = 'a'+word
        for i in range(len(word)-1):
            x = abs(ord(word[i]) - ord(word[i+1]))
            s = s + min(x, 26-x)
            
        return s