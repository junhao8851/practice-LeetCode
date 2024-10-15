class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp[i]定义为以nums[i]结尾的最大子数组之和

        # 初始化
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]  # 递推公式

        return max(dp)