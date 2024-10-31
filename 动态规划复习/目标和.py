class Solution
    def findTargetSumWays(self, nums List[int], target int) - int
         s = sum(nums) - abs(target)
         if s  0 or s % 2
            return 0
         m = s  2  # 背包容量
         
         @cache 

         def dfs(i int, c int) - int
            if i  0
                return 1 if c == 0 else 0
            if c  nums[i]
                return dfs(i - 1, c)  # 只能不选
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])  # 不选 + 选

         return dfs(len(nums) - 1, m)