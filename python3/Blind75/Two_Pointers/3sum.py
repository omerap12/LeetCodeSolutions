# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        tested_numbers = set()
        answer = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in tested_numbers:
                self.twoSum(nums, answer, i, -nums[i])
                tested_numbers.add(nums[i])
        return [v for v in answer]

    def twoSum(self, nums, answer, index, total):
        right_pointer = len(nums) - 1
        left_pointer = 0
        while left_pointer < right_pointer:
            if left_pointer == index:
                left_pointer += 1
                continue
            if right_pointer == index:
                right_pointer -= 1
                continue
            if nums[left_pointer] + nums[right_pointer] == total:
                add_to_answer = [nums[left_pointer], nums[right_pointer], -total]
                add_to_answer.sort()
                answer.add(tuple(add_to_answer))
                right_pointer -= 1
            elif nums[left_pointer] + nums[right_pointer] < total:
                left_pointer += 1
            else:
                right_pointer -= 1
