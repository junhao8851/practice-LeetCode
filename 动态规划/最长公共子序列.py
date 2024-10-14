class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]含义：nums1的前i-1个数和nums前j-1个数的最长公共子数组长度
        m, n = len(text1), len(text2)
        ans = 0
        #初始化
        dp = [[0]*(n+1) for _ in range(m+1) ] 
        for i in range(1 , m+1): #遍历顺序无所谓
            for j in range(1 , n+1):
                if text1[i-1] == text2[j-1]:
                    #递推公式
                    dp[i][j] = dp[i-1][j-1] + 1 
                    ans = max(ans , dp[i][j])
                    #以上代码跟上一题一致
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return ans