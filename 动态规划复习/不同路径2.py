class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid) # m为行数 
        n = len(obstacleGrid[0]) # n为列数
        # 如果终点或起点位置就有障碍，到达不了终点，直接return 0
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        # 初始化有所不同
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  # 对第一列初始化，遇到障碍物时，直接退出循环，后面默认都是0
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0: # 同上对第一行初始化
                dp[0][j] = 1
            else:
                break

        #遍历顺序和递推公式不变，只是要先判断该点是不是障碍，若是则略过该点
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]