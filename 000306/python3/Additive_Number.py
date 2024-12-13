class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(num):
                return len(stack) >= 3
            for j in range(i, len(num)):
                s = num[i:j + 1]
                if len(s) > 1 and s[0] == "0":
                    break
                stack.append(int(s))
                if len(stack) >= 3:
                    if stack[-1] == stack[-2] + stack[-3]:
                        if dfs(j + 1):
                            return True
                else:
                    if dfs(j + 1):
                        return True
                stack.pop()
            return False

        return dfs(0)
