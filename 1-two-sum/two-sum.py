class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        js = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in js:
                return [js[x], i]
            js[num] = i
        return []