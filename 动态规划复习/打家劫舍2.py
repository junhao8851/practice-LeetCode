class Solution:
    #rob1为打家劫舍1的算法，rob为打家劫舍2利用rob1实现的算法
        def rob1(self, nums: List[int]) -> int:
            if len(nums) == 0:  # 如果没有房屋，返回0
               return 0
            if len(nums) == 1:  # 如果只有一个房屋，返回其金额
               return nums[0]

        # 创建一个动态规划数组，用于存储最大金额
            dp = [0] * len(nums)
            dp[0] = nums[0]  # 将dp的第一个元素设置为第一个房屋的金额
            dp[1] = max(nums[0], nums[1])  # 将dp的第二个元素设置为第一二个房屋中的金额较大者

        # 遍历剩余的房屋
            for i in range(2, len(nums)):
            # 对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]  # 返回最后一个房屋中可抢劫的最大金额


        def rob(self, nums: List[int]) -> int:
            return max(nums[0] + self.rob1(nums[2:-1]) , self.rob1(nums[1:])) #考虑进第一个而不考虑最后一个，或者不考虑第一个而考虑进最后一个