from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        cache = [False for _ in range(target + 1)]
        cache[0] = True
        for num in nums:
            for i in range(target, -1, -1):
                if i < num or cache[i]:
                    continue
                else:
                    cache[i] = cache[i - num]
            if cache[-1]:
                return True
        return cache[-1]
