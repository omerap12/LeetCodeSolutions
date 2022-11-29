# https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums):
        dp = [float('inf')]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            dp[i] = 1 + min(dp[i+j] for j in range(nums[i]+1) if i+j<len(nums))
        return dp[0]
