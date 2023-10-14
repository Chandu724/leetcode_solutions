class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,j in enumerate(nums):
        #     for k,l in enumerate(nums[i+1:]):
        #         if j+l == target:
        #             return [i,k+i+1]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            


        
