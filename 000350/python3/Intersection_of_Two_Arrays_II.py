from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = dict()
        map2 = dict()
        for num in nums1:
            map1[num] = map1.get(num, 0) + 1
        for num in nums2:
            map2[num] = map2.get(num, 0) + 1
        result = list()
        for num, c in map1.items():
            if num in map2:
                count = min(c, map2[num])
                for _ in range(count):
                    result.append(num)
        return result
