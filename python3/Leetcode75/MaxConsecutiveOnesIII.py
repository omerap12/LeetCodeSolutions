# https://leetcode.com/problems/max-consecutive-ones-iii/description/
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        sliding_window = []
        number_of_zeroes = 0
        ret = 0

        for num in nums:
            if num == 1:
                sliding_window.append(num)
                ret = max(len(sliding_window),ret)
            else:
                if number_of_zeroes < k:
                    sliding_window.append(num)
                    number_of_zeroes += 1
                else:
                    sliding_window.append(num)
                    number_of_zeroes += 1
                    
                    while number_of_zeroes > k:
                        popped_number = sliding_window.pop(0)
                        if popped_number == 0:
                            number_of_zeroes -= 1
                ret = max(len(sliding_window),ret)
        ret = max(len(sliding_window),ret)
        return ret