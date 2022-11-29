# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        curr = 0
        for number in nums:
            curr += number
            max_sum = max(max_sum,curr)
            if curr < 0:
                curr = 0
        return max_sum
