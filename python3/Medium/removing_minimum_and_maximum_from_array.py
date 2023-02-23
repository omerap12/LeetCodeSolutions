# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/

from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        """
        First we find the minimum and maximum values in the list and their indexes and backward indexes.
        Then we have 4 options->
        1. get the min and max values by their normal indexes.
        2. get the min and max values by their backward indexes.
        3. get the min by the front and max by the back
        4. get the max by the front and min by the back
        we return the min between the 4 options
        :param nums: numbers
        :return: the min operations to remove the min and max values of the list.
        """
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        max_value = max(nums)
        min_value = min(nums)
        min_index = [nums.index(min_value), len(nums) - 1 - nums.index(min_value)]
        max_index = [nums.index(max_value), len(nums) - 1 - nums.index(max_value)]
        forward_forward = max(max_index[0], min_index[0]) + 1
        backward_backward = max(max_index[1], min_index[1]) + 1
        forward_backward = max_index[0] + min_index[1] + 2
        backward_forward = max_index[1] + min_index[0] + 2
        return min(forward_forward, backward_backward, forward_backward, backward_forward)