class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1

        for i in range(1,m):
            for ii in range(1,n):
                if obstacleGrid[i][ii] == 1:
                    dp[i][ii] = 0
                else:
                    dp[i][ii] = dp[i - 1][ii] + dp[i][ii - 1]

        return dp[m - 1][n -1]