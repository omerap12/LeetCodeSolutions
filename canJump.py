solution To: https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        distance_from_target = nums[0]
        index_start = 0
        finish_index = len(nums)-1

        if finish_index == 0:
            return True

        for i in range(finish_index):
            if distance_from_target + index_start >= finish_index:
                return True
            distance_from_target = max(distance_from_target,nums[i])
            distance_from_target = distance_from_target - 1
            if distance_from_target < 0:
                return False
        return True
