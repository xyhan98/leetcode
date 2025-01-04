from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int):
            if not 0 <= i < m or not 0 <= j < n or (i, j) in visit or grid[i][j] == 0:
                return 0
            visit.add((i, j))
            res = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = max(res, dfs(i + di, j + dj))
            visit.remove((i, j))
            return res + grid[i][j]
        
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                visit = set()
                total = dfs(i, j)
                result = max(result, total)
        return result
