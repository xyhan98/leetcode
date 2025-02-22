from typing import List


class Solution:
    # Time Limit Exceeded
    def maxRotateFunction(self, nums: List[int]) -> int:
        cache = dict()
        for num in nums:
            acc = 0
            vals = [0]
            if num in cache:
                continue
            for _ in range(1, len(nums)):
                acc += num
                vals.append(acc)
            cache[num] = vals

        result = sum([cache[num][i] for i, num in enumerate(nums)])
        for i in range(1, len(nums)):
            result = max(result, sum([cache[num][i] for i, num in enumerate(nums[-i:] + nums[:-i])]))
        return result
    
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        result = sum([i * num for i, num in enumerate(nums)])
        prev = result
        for i in range(1, n):
            curr = prev + total - nums[-i] * n
            result = max(result, curr)
            prev = curr
        return result
