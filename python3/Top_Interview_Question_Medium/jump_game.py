# https://leetcode.com/problems/jump-game/
class Solution(object):
    """
    instead of starting from one point and check if you can reach to the end.
    start from the end and check if you can get to the start.
    """
    def canJump(self, nums):
        stop_index = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= stop_index:
                stop_index = i
        return stop_index == 0
