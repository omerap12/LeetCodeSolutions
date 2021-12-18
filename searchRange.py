Solution To: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:  # for empty array
            return [-1, -1]
        if len(nums) == 1:  # for size one array
            return [0, 0] if nums[0] == target else [-1, -1]
        if len(nums) == 2:  # for size two array
            is_first = True if nums[0] == target else False
            is_second = True if nums[1] == target else False
            if is_first and is_second:
                return [0, 1]
            if is_first:
                return [0, 0]
            if is_second:
                return [1, 1]
            else:
                return [-1, -1]

        min_index = self.find_min_index(nums, 0, len(nums) - 1, target)
        max_index = self.find_max_index(nums, 0, len(nums) - 1, target)
        return [min_index, max_index]

    def find_min_index(self, nums, low_index, high_index, target):
        """
        using binary search algorithm, checking if the left number next to out chosen number is different if so It's
        the min index else recursively go left
        :param nums: sorted numbers array
        :param low_index: for binary search algorithm
        :param high_index: for binary search algorithm
        :param target: the value requested
        :return: the starting position of target in the array
        """
        middle_index = int((low_index + high_index) / 2)  # get the middle index
        if middle_index == low_index and middle_index == high_index:  # if one element only remain
            if nums[middle_index] == target:
                return middle_index
            else:
                return -1
        if nums[middle_index] == target and nums[middle_index - 1] != target:  # if the value to the left is different
            return middle_index
        if nums[middle_index] == target and nums[middle_index - 1] == target:  # if not
            if middle_index - 1 >= 0:  # for bounding reasons
                middle_index -= 1
            else:
                middle_index = 0
            return self.find_min_index(nums, 0, middle_index, target)  # go left
        elif nums[middle_index] > target:
            return self.find_min_index(nums, 0, middle_index - 1, target)
        else:
            return self.find_min_index(nums, middle_index + 1, high_index, target)

    def find_max_index(self, nums, low_index, high_index, target):
        """
        using binary search algorithm, checking if the right number next to out chosen number is different if so It's
        the max index else recursively go right
        :param nums: sorted numbers array
        :param low_index: for binary search algorithm
        :param high_index: for binary search algorithm
        :param target: the value requested
        :return: the ending position of target in the array
        """
        middle_index = int((low_index + high_index) / 2)  # get the middle index
        if middle_index == low_index and middle_index == high_index:  # if one element only remain
            if nums[middle_index] == target:
                return middle_index
            else:
                return -1
        if nums[middle_index] == target and nums[middle_index + 1] != target:  # if the value to the right is different
            return middle_index
        if nums[middle_index] == target and nums[middle_index + 1] == target:  # if not
            return self.find_max_index(nums, middle_index + 1, high_index, target)  # go right
        elif nums[middle_index] > target:
            if middle_index - 1 >= 0:
                return self.find_max_index(nums, 0, middle_index - 1, target)
        else:
            return self.find_max_index(nums, middle_index + 1, high_index, target)
