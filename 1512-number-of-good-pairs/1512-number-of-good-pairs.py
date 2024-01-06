class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        di = {}
        for i in range(len(nums)):
            if nums[i] in di.keys():
                di[nums[i]] = di[nums[i]] + 1
            else:
                di[nums[i]] = 0
                
                
        x=0
        for i in di.keys():
            x = x + di[i]*(di[i] + 1)//2
            
        return x
            
        