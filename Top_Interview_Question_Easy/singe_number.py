# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        answer = nums[0]
        for i in range(1,len(nums),1):
            answer = answer ^ nums[i]
        return answer