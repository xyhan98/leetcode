from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = list()
        cols = set()
        diagP = set()
        diagN = set()

        def dfs(i: int):
            if i == n:
                res = ["".join(r) for r in board]
                result.append(res)
                return
            for j in range(n):
                if j not in cols and i - j not in diagN and i + j not in diagP:
                    cols.add(j)
                    diagN.add(i - j)
                    diagP.add(i + j)
                    board[i][j] = "Q"
                    dfs(i + 1)
                    board[i][j] = "."
                    diagP.remove(i + j)
                    diagN.remove(i - j)
                    cols.remove(j)
        
        dfs(0)
        return result
