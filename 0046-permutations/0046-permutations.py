class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(perms):
            if len(perms) == len(nums):
                res.append(perms[:])
                return
            
            for n in nums:
                if n not in perms:
                    perms.append(n)
                    backtrack(perms)
                    perms.pop()
        
        backtrack([])
        return res