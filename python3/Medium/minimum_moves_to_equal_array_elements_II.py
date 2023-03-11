# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Obesrvation: The middle number will give us the lowest value  
        """
        nums.sort()
        res = 0
        mid_number = nums[len(nums)//2]
        for number in nums:
            res += abs(number-mid_number)
        return res
