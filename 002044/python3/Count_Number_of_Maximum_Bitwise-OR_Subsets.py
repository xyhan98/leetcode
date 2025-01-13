from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        results = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                if stack:
                    results.append(reduce(lambda x, y: x | y, stack))
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)
        
        dfs(0)
        maxOr = max(results)
        return results.count(maxOr)
