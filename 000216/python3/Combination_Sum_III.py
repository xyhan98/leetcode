from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = list()
        if n > (1 + 9) * 9 // 2:
            return result
        stack = list()

        def dfs(i: int, sum: int):
            if sum == n and len(stack) == k:
                result.append(list(stack))
            if sum >= n or len(stack) >= k:
                return
            for j in range(i, 10):
                stack.append(j)
                dfs(j + 1, sum + j)
                stack.pop()
        
        dfs(1, 0)
        return result
