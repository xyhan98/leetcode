from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        
        def dfs(i: int, sum: int):
            if i == len(nums):
                if sum == target:
                    nonlocal result
                    result += 1
                return
            dfs(i + 1, sum + nums[i])
            dfs(i + 1, sum - nums[i])
        
        dfs(0, 0)
        return result

# Time Limit Exceeded (Backtracking)
