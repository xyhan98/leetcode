from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        stack = list()

        def dfs(i: int):
            if len(stack) >= 2 and stack[-1] < stack[-2]:
                return
            if i == len(nums):
                if len(stack) >= 2:
                    result.add(tuple(stack))
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)

        dfs(0)
        result = list(map(list, result))
        # print(result)
        return result

s = Solution()
s.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
