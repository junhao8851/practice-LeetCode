class Solution:
    def fib(self, n: int) -> int:
#边缘情况
        if n == 0:
            return 0
#初始化
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
#遍历顺序（由递推关系决定）
        for i in range(2,n+1): 
            dp[i] = dp[i-1] + dp[i-2] #递推关系
        
        return dp[n]