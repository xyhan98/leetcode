class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        cols = set()
        diagP = set()
        diagN = set()

        def dfs(i: int):
            if i == n:
                nonlocal result
                result += 1
                return
            for j in range(n):
                if j in cols or i + j in diagP or i - j in diagN:
                    continue
                cols.add(j)
                diagP.add(i + j)
                diagN.add(i - j)
                dfs(i + 1)
                diagN.remove(i - j)
                diagP.remove(i + j)
                cols.remove(j)
        
        dfs(0)
        return result
