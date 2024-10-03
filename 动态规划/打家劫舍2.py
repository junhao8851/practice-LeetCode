class Solution:

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i): # 表示前i个房子可以偷到的最大值
            if i < 0:
                return 0

            res = max(dfs(i-1) , dfs(i-2) + nums[i])
            return res

        return dfs(n-1)

    def rob(self, nums: List[int]) -> int:
        #与打家劫舍1的区别仅仅在于需要分类讨论是否偷nums[0]
        return max(nums[0] + self.rob1(nums[2:-1] ), self.rob1(nums[1:]))