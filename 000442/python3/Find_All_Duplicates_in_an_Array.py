from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        hashset = set()
        for num in nums:
            if num in hashset:
                result.append(num)
            else:
                hashset.add(num)
        return result
