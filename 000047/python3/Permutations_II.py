from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashmap = dict()
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                result.append(list(stack))
                return
            for num, count in hashmap.items():
                if count == 0:
                    continue
                hashmap[num] -= 1
                stack.append(num)
                dfs(i + 1)
                stack.pop()
                hashmap[num] += 1
        
        dfs(0)
        return result
