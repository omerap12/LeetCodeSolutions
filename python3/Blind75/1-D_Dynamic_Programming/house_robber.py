# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [-float('inf')]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2,len(nums),1):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[len(nums)-1]
