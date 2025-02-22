class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cache = [[False for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for j in range(len(t) + 1):
            cache[-1][j] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = cache[i][j + 1]
        return cache[0][0]
