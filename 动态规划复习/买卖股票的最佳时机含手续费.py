class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 持有股票手上的最大現金
        hold = -prices[0] - fee
        # 不持有股票手上的最大現金
        not_hold = 0
        for price in prices[1:]:
            new_hold = max(hold, not_hold - price - fee)
            new_not_hold = max(not_hold, hold + price)
            hold, not_hold = new_hold, new_not_hold
        return not_hold