# https://leetcode.com/problems/3sum/submissions/
class Solution(object):
    def threeSum(self, nums):
        answer = set()
        answer_list = []
        """
        instead of checking for numbers that already have been checked, save the numbers that have been checked in
        set, if the number is already in set pass.
        """
        numbers_checked = set()
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] not in numbers_checked:
                numbers_checked.add(sorted_nums[i])
                """
                calculating two sum for (sum is -number for every number in the array)
                """
                self.two_sum(i, sorted_nums[i], sorted_nums, answer, answer_list)
        return answer_list

    def two_sum(self, index, number, nums_sorted, answer, answer_list):
        two_sum_output = []
        start_pointer = 0
        stop_pointer = len(nums_sorted) - 1
        while start_pointer < stop_pointer:
            if start_pointer == index:
                start_pointer += 1
            if stop_pointer == index:
                stop_pointer -= 1
            if start_pointer == stop_pointer:
                continue
            if nums_sorted[start_pointer] + nums_sorted[stop_pointer] == -number:
                triple_to_add = sorted([nums_sorted[start_pointer], nums_sorted[stop_pointer], number])
                if tuple(triple_to_add) not in answer:
                    answer.add(tuple(triple_to_add))
                    answer_list.append(triple_to_add)
                stop_pointer -= 1
            elif nums_sorted[start_pointer] + nums_sorted[stop_pointer] < -number:
                start_pointer += 1
            else:
                stop_pointer -= 1
        return two_sum_output
