from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(s):
                result.append("".join(stack))
                return
            j = 0
            while i + j < len(s) and s[i + j].isnumeric():
                stack.append(s[i + j])
                j += 1
            if i + j < len(s):
                stack.append(s[i + j].lower())
                dfs(i + j + 1)
                stack.pop()
                stack.append(s[i + j].upper())
                dfs(i + j + 1)
                stack.pop()
            else:
                dfs(i + j)
            for _ in range(j):
                stack.pop()

        dfs(0)
        return result
