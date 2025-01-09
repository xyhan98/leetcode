class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0

        def dfs(i: int) -> bool:
            if i == len(s):
                return sum(stack) == copy
            for j in range(1, len(s) + 1 - i):
                c = s[i:i + j]
                if j > 1 and c[0] == "0":
                    continue
                stack.append(int(c))
                if dfs(i + j):
                    return True
                stack.pop()
            return False

        for i in range(1, n + 1):
            copy = i
            num = i**2
            s = str(num)
            stack = list()
            if dfs(0):
                result += num
        
        return result
