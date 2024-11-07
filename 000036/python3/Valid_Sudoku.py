from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            row = set()
            for j in range(n):
                c = board[i][j]
                if c == ".":
                    continue
                elif c in row:
                    return False
                row.add(c)
        
        for j in range(n):
            col = set()
            for i in range(m):
                c = board[i][j]
                if c == ".":
                    continue
                elif c in col:
                    return False
                col.add(c)
        
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = set()
                for di in range(3):
                    for dj in range(3):
                        c = board[i + di][j + dj]
                        if c == ".":
                            continue
                        elif c in box:
                            return False
                        box.add(c)
        
        return True
