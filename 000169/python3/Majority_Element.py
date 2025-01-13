from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        k, v = 0, 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if v < hashmap[num]:
                v = hashmap[num]
                k = num
        return k
        