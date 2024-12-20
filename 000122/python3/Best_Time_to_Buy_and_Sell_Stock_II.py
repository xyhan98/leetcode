from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result

"""
[1, 2, 3, 6] or [1, 3, 3, 6]
buy on the first day and sell on the last day
is the same as
buy on each day and sell on the next day if the profit is greater than 0
but not same for
[1, 4, 3, 6]
"""
