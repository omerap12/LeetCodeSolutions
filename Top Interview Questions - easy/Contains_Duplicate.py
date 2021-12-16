Solution To: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return False
        if len(nums) == 2:
            return nums[0] == nums[1]
        sorted_nums = sorted(nums)
        first_number = sorted_nums[0]
        if len(nums) == 2:
            return
        for i in range(1, len(nums), 1):
            if sorted_nums[i] == first_number:
                return True
            else:
                first_number = sorted_nums[i]
        return False
