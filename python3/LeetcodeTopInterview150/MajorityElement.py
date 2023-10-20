# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List

# O(1) space solution, linear time, bayer-moores algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0],1
        for i in range(1,len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate