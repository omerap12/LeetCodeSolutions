# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target, nums):
        """
        Sliding window technique
        """
        window = []
        res = float('inf')
        current_sum_window = 0
        for number in nums:
            if current_sum_window < target:
                window.append(number)
                current_sum_window += number
            else:
                res = min(res,len(window))
                window.append(number)
                current_sum_window += number
                while window:
                    number_to_pop = window[0]
                    if current_sum_window - number_to_pop >= target:
                        window.pop(0)
                        current_sum_window -= number_to_pop
                    else:
                        break
                res = min(res, len(window))
        if current_sum_window >= target:
            while window:
                number_to_pop = window[0]
                if current_sum_window - number_to_pop >= target:
                    window.pop(0)
                    current_sum_window -= number_to_pop
                else:
                    break
            res = min(res, len(window))
        return res if res != float('inf') else 0
