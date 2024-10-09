class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 本题的思路和最佳时机2一样，只需要在买入（或者卖出）的时候，额外减去手续费 fee 作为开销
        n = len(prices)
        @cache  
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i] - fee)

        return dfs(n - 1, False)