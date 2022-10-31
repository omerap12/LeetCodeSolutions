# https://leetcode.com/problems/maximum-product-subarray/submissions/

class Solution:
    def maxProduct(self, nums):
        temp_max = 1
        temp_min = 1
        max_answer = max(nums)
        for number in nums:
            if number == 0:
                temp_max = 1
                temp_min = 1
            else:
                curr = temp_max * number
                temp_max = max(curr, temp_min * number, number)
                temp_min = min(curr, temp_min * number, number)
                max_answer = max(max_answer,temp_max)
        return max_answer
