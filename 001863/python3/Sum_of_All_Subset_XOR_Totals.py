from functools import reduce
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                if stack:
                    nonlocal result
                    result += reduce(lambda x, y: x ^ y, stack)
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)
        
        dfs(0)
        return result
