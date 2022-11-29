# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    """
    Google job interview question!!!
    The key is to find the begging of every sequence.
    """
    def longestConsecutive(self, nums):
        set_nums = set(nums)
        set_nums_without_left_neighbor = set()
        max_counter = 0
        # finding the start of every sequence
        for number in nums:
            if number-1 not in set_nums and number-1 not in set_nums_without_left_neighbor:
                set_nums_without_left_neighbor.add(number)
        # counting the sequence
        for number in set_nums_without_left_neighbor:
            counter = 0
            current_number = number
            while current_number in set_nums:
                counter += 1
                current_number += 1
                max_counter = max(counter,max_counter)
        return max_counter
