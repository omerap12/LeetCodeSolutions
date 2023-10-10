# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix,suffix = [],[]
        curr = 0
        for number in nums:
            prefix.append(curr)
            curr += number
        
        curr = 0
        for number in nums[::-1]:
            suffix.append(curr)
            curr += number
        suffix.reverse()

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        
        return -1