from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()

        def dfs(i: int, sum: int) -> int:
            if i == len(nums):
                return 1 if sum == target else 0
            if (i, sum) in cache:
                return cache[(i, sum)]
            cache[(i, sum)] = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
            return cache[(i, sum)]

        return dfs(0, 0)

s = Solution()
s.findTargetSumWays([1, 1, 1, 1, 1], 3)
