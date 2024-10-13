class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #dp[i][j]含义：nums1的前i-1个数和nums前j-1个数的最长公共子数组长度
        m, n = len(nums1), len(nums2)
        ans = 0
        #初始化
        dp = [[0]*(n+1) for _ in range(m+1) ] 
        for i in range(1 , m+1): #遍历顺序无所谓
            for j in range(1 , n+1):
                if nums1[i-1] == nums2[j-1]:
                    #递推公式
                    dp[i][j] = dp[i-1][j-1] + 1 
                    ans = max(ans , dp[i][j])
        
        return ans