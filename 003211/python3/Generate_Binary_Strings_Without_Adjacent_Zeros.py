from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = list()
        stack = list()

        def dfs(i: int):
            if i == n:
                result.append("".join(stack))
                return
            if not stack or stack[-1] == "1":
                stack.append("0")
                dfs(i + 1)
                stack.pop()
            stack.append("1")
            dfs(i + 1)
            stack.pop()
        
        dfs(0)
        return result
