class Solution:
    def reverse(self, x: int) -> int:
        
        x = list(str(x))
        x = x[::-1]
        
        while x[0] == '0' and len(x) > 1:
            x.pop(0)
            
        if x[-1] == '-':
            x.pop(-1)
            x =  int('-' + ''.join(x))
        else:
            x = int(''.join(x))
            
        if x <= 2**31 - 1 and -2**31 <= x:
            return x
        else:
            return 0