from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        cols = list()
        stack = list()

        def dfs(i: int, c: int):
            if c == numSelect:
                cols.append(set(stack))
                return
            if i == n:
                return
            stack.append(i)
            dfs(i + 1, c + 1)
            stack.pop()
            dfs(i + 1, c)
        
        dfs(0, 0)
        # print(cols)
        rows = list()
        for i in range(m):
            col = set()
            for j in range(n):
                if matrix[i][j] == 1:
                    col.add(j)
            rows.append(col)
        
        result = 0
        for col in cols:
            res = 0
            for row in rows:
                if row:
                    if not (row - col):
                        res += 1
                else:
                    res += 1
            result = max(result, res)

        return result
