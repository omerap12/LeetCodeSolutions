# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins,amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        min_prev = float('inf')
        for i in range(1,amount+1,1):
            for c in coins:
                if i-c >= 0:
                    min_prev = min(min_prev,dp[i-c])
            dp[i] = 1+min_prev
            min_prev = float('inf')
        return dp[amount] if dp[amount] != float('inf') else -1
