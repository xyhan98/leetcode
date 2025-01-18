from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        result = list()
        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)
        return result
