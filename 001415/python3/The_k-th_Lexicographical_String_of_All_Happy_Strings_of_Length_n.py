class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = list()
        stack = list()

        def dfs(i: int):
            if i == n:
                result.append("".join(stack))
                return
            for c in "abc":
                if not stack or (stack and stack[-1] != c):
                    stack.append(c)
                    dfs(i + 1)
                    stack.pop()
                

        dfs(0)
        return result[k - 1] if len(result) >= k else ""
