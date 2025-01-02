class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = 0
        stack = list()

        def dfs(i: int):
            if i == len(s):
                nonlocal result
                result = max(result, len(stack))
                return
            for j in range(1, len(s) + 1 - i):
                t = s[i: i + j]
                if t in stack:
                    continue
                stack.append(t)
                dfs(i + j)
                stack.pop()
        
        dfs(0)
        return result
