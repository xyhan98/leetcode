from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [False for _ in nums]
        cache[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                if cache[i + j]:
                    cache[i] = True
                    break
        return cache[0]
