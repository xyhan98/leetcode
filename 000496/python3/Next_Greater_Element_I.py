from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = [-1 for _ in nums2]
        stack = list()
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                j = stack.pop()
                nums3[j] = num
            stack.append(i)
        hashmap = {i: j for i, j in zip(nums2, nums3)}
        result = list()
        for num in nums1:
            result.append(hashmap[num])
        return result
