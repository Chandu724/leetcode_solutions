class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        x = sorted(nums, reverse=True)
        
        k = 0
        while k < len(x):
            temp = x.count(x[k])
            if temp == 1:
                return x[k]
            else:
                k = k + temp
                
        return -1