from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[m - 1][n - 1] = 1 - obstacleGrid[m - 1][n - 1]
        for j in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][j] == 1:
                obstacleGrid[m - 1][j] = 0
            else:
                obstacleGrid[m - 1][j] = obstacleGrid[m - 1][j + 1]
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                obstacleGrid[i][n - 1] = 0
            else:
                obstacleGrid[i][n - 1] = obstacleGrid[i + 1][n - 1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] += obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
        return obstacleGrid[0][0]
