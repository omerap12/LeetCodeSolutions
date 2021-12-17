Solution To: https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        INFINITE = float('inf')  # declaring positive infinite
        dynamic_array = [INFINITE] * (amount + 1)  # creating list for 0-amount coins
        dynamic_array[0] = 0  # need 0 coins for 0 amount

        for i in range(1, amount + 1):
            dynamic_array[i] = min(dynamic_array[i - c] if i - c >= 0 else INFINITE for c in coins) + 1 # based on Knapsack problem get the min value betwwen taking the coin and not taking the coin, if can't reach current val put INF

        if dynamic_array[amount] != INFINITE: # required value is at the dynamic_array[amount] , if not infinte means we can reach that value
            return dynamic_array[amount]
        return -1
