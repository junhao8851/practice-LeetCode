class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        #初始化：对角线初始化为1，其余为0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1 #当i==j时，dp初始化为1

        #遍历顺序：i从下到上，j从左到右
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                #递推公式
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]