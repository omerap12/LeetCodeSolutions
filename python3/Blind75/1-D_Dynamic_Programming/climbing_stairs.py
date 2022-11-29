# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        dp = [0]*(n+1)
        for i in range(n+1):
            dp[i] = 1 if i-2 < 0 else dp[i-1]+dp[i-2]
        return dp[n]
