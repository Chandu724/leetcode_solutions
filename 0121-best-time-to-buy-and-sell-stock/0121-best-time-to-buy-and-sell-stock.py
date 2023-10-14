class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_p = 0
        min_p = sum(prices)
        
        for i in prices:
            if i < min_p:
                min_p = i
            if i - min_p > max_p:
                max_p = i - min_p
        return max_p
        