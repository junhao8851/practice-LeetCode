class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[i][j]表示初始点到（i，j）的路径数
        dp =[[0] * n for _ in range(m)]
        #初始化
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        #遍历顺序
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] #递推公式
        
        return dp[m-1][n-1]