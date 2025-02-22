from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        if len(nums) < 3:
            return result
        i, j = 0, 2
        diff = nums[1] - nums[0]
        while j < len(nums):
            diff1 = nums[j] - nums[j - 1]
            if diff1 != diff:
                if j - i >= 3:
                    k = 3
                    while k <= j - i:
                        result += (j - i) - (k - 1)
                        k += 1
                diff = diff1
                i = j - 1
            j += 1
        if j - i >= 3:
            k = 3
            while k <= j - i:
                result += (j - i) - (k - 1)
                k += 1
        return result
