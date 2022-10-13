# https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        Kaden's Algorithm
        """
        max_sum = float('-inf')
        current_sum = 0
        for number in nums:
            current_sum += number
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
