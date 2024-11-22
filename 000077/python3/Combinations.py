from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        stack = list()

        def dfs(i: int, num: int):
            if num == k:
                result.append(list(stack))
                return
            if i == n + 1:
                return
            stack.append(i)
            dfs(i + 1, num + 1)
            stack.pop()
            dfs(i + 1, num)
        
        dfs(1, 0)
        return result
