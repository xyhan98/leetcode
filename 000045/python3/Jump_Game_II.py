from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [float('inf') for _ in nums]
        cache[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                continue
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                cache[i] = min(cache[i], cache[i + j] + 1)
        return cache[0]
