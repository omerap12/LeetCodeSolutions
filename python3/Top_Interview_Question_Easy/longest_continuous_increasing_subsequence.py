# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums):
        window = []
        max_size = 0
        for number in nums:
            if not window:
                window.append(number)
            else:
                if window[-1] < number:
                    window.append(number)
                else:
                    window.clear()
                    window.append(number)
            max_size = max(max_size,len(window))
        return max_size
