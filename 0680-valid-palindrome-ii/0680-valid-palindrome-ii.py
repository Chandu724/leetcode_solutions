class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        
        s = list(s)
        while len(s) > 0:
            if s[0] == s[-1]:
                s.pop(0)
                s.pop(-1)
            else:
                x = s[1:]
                y = s[:-1]
                
                if x == x[::-1] or y == y[::-1]:
                    return True
                else:
                    return False
        
        return True