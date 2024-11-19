from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        integers = set(nums)
        result = 0

        for num in nums:
            if num not in integers:
                continue
            if num - 1 not in integers:
                i = 0
                while num + i in integers:
                    integers.remove(num + i)
                    i += 1
                result = max(result, i)
        return result
