from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def dp(vals: List[int]) -> int:
            vals[1] = max(vals[1], vals[0])
            for i in range(2, len(vals)):
                vals[i] = max(vals[i - 1], vals[i] + vals[i - 2])
            return vals[-1]
        
        return max(dp(nums[:-1]), dp(nums[1:]))
