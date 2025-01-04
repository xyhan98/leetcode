from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = list()
        stack = list()

        def dfs(i: int):
            if i == n:
                result.append(int("".join(map(str, stack))))
                return
            start = 1 if i == 0 else 0
            for j in range(start, 10):
                if not stack or abs(stack[-1] - j) == k:
                    stack.append(j)
                    dfs(i + 1)
                    stack.pop()

        dfs(0)
        return result
