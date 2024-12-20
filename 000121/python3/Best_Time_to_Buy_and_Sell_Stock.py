from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = prices[-1]
        prices[-1] = 0
        for i in range(len(prices) - 2, -1, -1):
            if maxPrice >= prices[i]:
                prices[i] = maxPrice - prices[i]
            else:
                maxPrice = prices[i]
                prices[i] = 0
        return max(prices)
