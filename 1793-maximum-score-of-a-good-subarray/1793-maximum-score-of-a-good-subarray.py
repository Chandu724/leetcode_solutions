class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = nums[k]
        mr = nums[k]
        n = len(nums)
        
        i = k - 1
        j = k + 1
        
        while i != -1 or j != n:
            x = nums[i] if i!=-1 else 0
            y = nums[j] if j!=n else 0
            
            if x < y:
                mr = min(mr, nums[j])
                j = j + 1
                
            else:
                mr = min(mr, nums[i])
                i = i - 1
                
            print(i,j,mr,res)
            res = max(res, mr*(j - i - 1))
            
            
        return res
        
    