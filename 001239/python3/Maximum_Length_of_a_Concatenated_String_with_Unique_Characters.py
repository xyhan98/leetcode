from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        stack = list()

        def dfs(i: int):
            if i == len(arr):
                nonlocal result
                result = max(result, len("".join(stack)))
                return
            stack.append(arr[i])
            s = "".join(stack)
            if len(s) == len(set(list(s))):
                dfs(i + 1)
            stack.pop()
            dfs(i + 1)
            
        dfs(0)
        return result
