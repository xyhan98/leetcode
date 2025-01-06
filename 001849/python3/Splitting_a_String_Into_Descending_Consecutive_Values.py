class Solution:
    def splitString(self, s: str) -> bool:
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(s):
                return True if len(stack) >= 2 else False
            for j in range(1, len(s) + 1 - i):
                t = int(s[i: i + j])
                if not stack or stack[-1] - 1 == t:
                    stack.append(t)
                    if dfs(i + j):
                        return True
                    stack.pop()
            return False
        
        return dfs(0)
