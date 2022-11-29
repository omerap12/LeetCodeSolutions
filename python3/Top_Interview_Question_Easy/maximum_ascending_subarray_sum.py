# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums):
        window = []
        max_sum = 0
        for number in nums:
            if not window:
                window.append(number)
            else:
                if window[-1] < number:
                    window.append(number)
                else:
                    window.clear()
                    window.append(number)
            max_sum = max(max_sum,sum(window))
        return max_sum
