# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Just perform 2-sum.
        :return:
        """
        ret = 0
        nums.sort()
        lptr, rptr = 0, len(nums) - 1
        while lptr < rptr:
            if nums[lptr] + nums[rptr] < k:
                lptr += 1
            elif nums[lptr] + nums[rptr] > k:
                rptr -= 1
            else:
                ret += 1
                lptr += 1
                rptr -= 1
        return ret