class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #只要求返回最大和的值，不要求得到最大的连续子数组是哪一个，这种某个值不断尝试更新的问题通常考虑动态规划

        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
