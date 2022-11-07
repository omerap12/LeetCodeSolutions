# solution To: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        # using kadane algorithm
        maxSum = nums[0]
        tempSum = 0

        for number in nums:
         # if prefix is negarive
            if tempSum < 0:
                tempSum = 0
            tempSum += number
            maxSum = max(maxSum,tempSum)
        return maxSum


