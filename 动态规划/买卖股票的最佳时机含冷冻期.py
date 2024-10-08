class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 和最佳时机2的区别仅在于买入的前一天必定是未持有的（包括卖出日），故持有时的两种情况稍有变动

        n = len(prices)
        @cache  
        def dfs(i: int, hold: bool) -> int:

            if i < 0: # 边界条件 把dfs(-1，1)这个不合法数据定为-inf
                return -inf if hold else 0

            if hold: 
                # 第i天持有股票，到第i天的利润分两种情况，即第i-1本就持有且不卖，或第i-2天未持有，到第i天买入
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            else: 
                # 第i天持有股票，到第i天的利润也分两种情况
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)