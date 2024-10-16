class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0

        # 遍历顺序，二维的dp从左下到右上递推（这是由递推关系决定的）
        for i in range(len(s)-1, -1, -1): 
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: # i,j相等或相邻
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: # i，j中间至少有一位
                        result += 1
                        dp[i][j] = True

        return result