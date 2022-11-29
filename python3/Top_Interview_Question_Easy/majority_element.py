# https://leetcode.com/problems/majority-element/
class Solution(object):
    def majorityElement(self, nums):
        counter_dict = {}
        for number in nums:
            if number in counter_dict.keys():
                counter_dict[number] += 1
            else:
                counter_dict[number] = 1
            if counter_dict[number] > len(nums) // 2:
                return number