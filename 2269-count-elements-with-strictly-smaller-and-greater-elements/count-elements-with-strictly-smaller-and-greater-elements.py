class Solution:
    def countElements(self, nums: List[int]) -> int:
        return max(len(nums) - nums.count(min(nums)) - nums.count(max(nums)), 0)