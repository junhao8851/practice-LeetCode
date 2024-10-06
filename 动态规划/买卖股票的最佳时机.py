class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 用ans保存最大差价
        ans = 0
        # 用min_price保存最低价
        min_pirce = prices[0]

        for i in prices: # 不断尝试更新两个变量
            ans = max(ans, p - min_pirce)
            min_pirce = min(min_pirce, p)

        return ans