from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = set()

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if not 0 <= i < m or not 0 <= j < n or (i, j) in visit or board[i][j] != word[k]:
                return False
            visit.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(i + di, j + dj, k + 1):
                    return True
            visit.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
