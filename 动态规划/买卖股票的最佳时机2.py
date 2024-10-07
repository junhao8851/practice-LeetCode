class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache  
        def dfs(i: int, hold: bool) -> int:

            if i < 0: # 边界条件 把dfs(-1，1)这个不合法数据定为-inf
                return -inf if hold else 0

            if hold: # 第i天持有股票，到第i天的利润分两种情况，前一天本就持有且不卖，或前一天未持有，到这一天买入
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            else: # 第i天持有股票，到第i天的利润也分两种情况
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)