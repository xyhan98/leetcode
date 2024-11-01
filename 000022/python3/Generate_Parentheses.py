from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        stack = list()

        def dfs(i: int, l: int, r: int):
            if i == 2 * n:
                result.append("".join(stack))
                return
            if l < n:
                stack.append("(")
                dfs(i + 1, l + 1, r)
                stack.pop()
            if l > r:
                stack.append(")")
                dfs(i + 1, l, r + 1)
                stack.pop()
            

        dfs(0, 0, 0)
        return result
