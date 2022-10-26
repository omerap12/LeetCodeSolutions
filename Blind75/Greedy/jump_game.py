# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        stop_index = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i >= stop_index:
                stop_index = i
        return stop_index == 0
