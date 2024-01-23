class Solution:
    def fib(self, n: int) -> int:
        def func(n):
            if n in [0,1]:
                return n
            return func(n-1) + func(n-2)
        
        return func(n)
        