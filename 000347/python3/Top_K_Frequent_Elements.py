from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        lst = [(v, k) for k, v in hashmap.items()]
        lst.sort(reverse=True)
        result = list()
        for i in range(k):
            result.append(lst[i][1])
        return result
