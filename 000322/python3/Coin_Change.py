from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1 for _ in range(amount + 1)]
        cache[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i < coin:
                    continue
                if cache[i - coin] != -1:
                    if cache[i] == -1:
                        cache[i] = cache[i - coin] + 1
                    else:
                        cache[i] = min(cache[i], cache[i - coin] + 1)
        return cache[-1]
