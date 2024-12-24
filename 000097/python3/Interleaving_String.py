class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = dict()

        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = False
            if i < len(s1) and s1[i] == s3[i + j]:
                cache[(i, j)] = dfs(i + 1, j)
            if cache[(i, j)]:
                return True
            if j < len(s2) and s2[j] == s3[i + j]:
                cache[(i, j)] = dfs(i, j + 1)
            return cache[(i, j)]
        
        return dfs(0, 0) if len(s1) + len(s2) == len(s3) else False
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        cache[-1][-1] = True
        for j in range(len(s2) - 1, -1, -1):
            cache[-1][j] = s2[j:] == s3[len(s1) + j:]
        for i in range(len(s1) - 1, -1, -1):
            cache[i][-1] = s1[i:] == s3[len(s2) + i:]
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s3[i + j]:
                    cache[i][j] = cache[i + 1][j]
                if cache[i][j]:
                    continue
                if s2[j] == s3[i + j]:
                    cache[i][j] = cache[i][j + 1]
        return cache[0][0]
