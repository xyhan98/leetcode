from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                result.append((list(stack)))
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            j = 0
            while i + j < len(nums) and nums[i + j] == nums[i]:
                j += 1
            dfs(i + j)
        
        dfs(0)
        return result
