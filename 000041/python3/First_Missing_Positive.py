from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        num = 1
        while nums:
            if num not in nums:
                break
            nums.remove(num)
            num += 1
        return num
