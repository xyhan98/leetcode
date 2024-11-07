from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = list()
        cols = list()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            rows.append(0 in set(matrix[i]))
        for j in range(n):
            cols.append(0 in {matrix[i][j] for i in range(m)})
        
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
