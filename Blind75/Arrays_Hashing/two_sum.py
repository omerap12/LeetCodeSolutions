# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        checked_number = set()
        for i in range(len(nums)):
            if nums[i] not in checked_number:
                checked_number.add(nums[i])
                for j in range(i+1,len(nums),1):
                    if nums[i] + nums[j
