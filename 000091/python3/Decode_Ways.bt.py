class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0

        def dfs(i: int):
            if i == len(s):
                nonlocal result
                result += 1
                return
            for j in [1, 2]:
                if i + j > len(s):
                    break
                code = s[i:i+j]
                if code[0] == "0":
                    break
                if len(code) == 2 and int(code) > 26:
                    break
                dfs(i + j)

        dfs(0)
        return result

# Time Limit Exceeded (Backtracking)
