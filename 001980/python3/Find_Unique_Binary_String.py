from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        stack = list()

        def dfs(i: int) -> bool:
            if i == n:
                return "".join(stack) not in nums
            for c in "01":
                stack.append(c)
                if dfs(i + 1):
                    return True
                stack.pop()
            return False
        
        dfs(0)
        return "".join(stack)
