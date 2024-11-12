from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashmap = {num: 1 for num in nums}
        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                result.append(list(stack))
                return
            for num, count in hashmap.items():
                if count == 0:
                    continue
                hashmap[num] = 0
                stack.append(num)
                dfs(i + 1)
                stack.pop()
                hashmap[num] = 1
        
        dfs(0)
        return result
