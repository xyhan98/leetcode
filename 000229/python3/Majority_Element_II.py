from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = 0
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            count += 1
        results = list()
        count //= 3
        for k, v in hashmap.items():
            if v > count:
                results.append(k)
        return results
        