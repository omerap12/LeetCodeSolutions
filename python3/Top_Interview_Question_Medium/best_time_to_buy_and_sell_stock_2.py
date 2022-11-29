# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the largest number minus the smallest number in each ascending subseries.
        Add the outcome to profit counter and return it
        """
        profit = 0
        current_profit = 0
        current_stock = prices[0]
        for i in range(len(prices)-1):
            # means the sock price is lower on the next. so if I have some profit ill save it now, beacuse in the future, 
            # if I would come accross a higher stock value I would need to buy this stock first to maximazie my profit
            if prices[i+1] < prices[i]:
                current_stock = prices[i+1]
                profit += current_profit
                current_profit = 0
            else:
                current_profit = max(prices[i+1] - current_stock,current_profit)
        profit += current_profit
        return profit
