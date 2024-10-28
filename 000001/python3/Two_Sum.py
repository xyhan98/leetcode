from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            if target - num not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[target - num], i]
