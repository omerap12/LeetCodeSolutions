# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        return True
