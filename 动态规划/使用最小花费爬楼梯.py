class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache  # 不用缓存装饰器会超时

        def dfs(i: int) -> int:

            if i <= 1:  # 递归边界
                return 0

            return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])

        return dfs(len(cost))