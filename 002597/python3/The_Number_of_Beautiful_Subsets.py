from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = -1 # non-empty
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                nonlocal result
                result += 1
                return
            if not stack or nums[i] - k not in set(stack):
                stack.append(nums[i])
                dfs(i + 1)
                stack.pop()
            dfs(i + 1)
        
        dfs(0)
        return result
