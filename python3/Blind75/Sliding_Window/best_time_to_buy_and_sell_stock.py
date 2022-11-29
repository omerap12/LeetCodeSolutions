# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        current_stock_price = prices[0]
        for i in range(1, len(prices), 1):
            max_profit = max(max_profit, prices[i] - current_stock_price)
            current_stock_price = min(current_stock_price, prices[i])
        return max_profit
