class Solution:
    def climbStairs(self, n: int) -> int:
        #不考虑dp[0]如何初始化，只初始化dp[1] = 1，dp[2] = 2，然后从i = 3开始递推，这样才符合dp[i]的定义
        #对于n==1的情况如果不单独return会导致dp定义的长度不够
        if n == 1:
            return 1 
        #初始化
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        #遍历顺序
        for i in range(3 , n+1):
            dp[i] = dp[i-1] + dp[i-2] #递推公式
        
        return dp[n]