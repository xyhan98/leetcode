from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1 for _ in nums]
        for i in range(len(nums) - 2, -1, -1):
            v = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    v = max(v, cache[j] + 1)
            cache[i] = v
        return max(cache)
