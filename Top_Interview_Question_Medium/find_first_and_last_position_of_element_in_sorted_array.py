# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        first_index = self.find_first_index(nums, target)
        if first_index == -1:
            return [-1, -1]
        return [first_index, self.find_second_index(nums, target)]

    def find_first_index(self, nums, target):
        start_index = 0
        stop_index = len(nums) - 1
        while start_index <= stop_index:
            mid = start_index+(stop_index-start_index) // 2
            if nums[mid] == target and mid-1 < 0:
                return mid
            if nums[mid] == target and nums[mid - 1] != target:
                return mid
            if nums[mid] == target and nums[mid - 1] == target:
                stop_index = mid - 1
            elif nums[mid] > target:
                stop_index = mid - 1
            elif nums[mid] < target:
                start_index = mid+1
            else:
                return None
        return -1

    def find_second_index(self, nums, target):
        if len(nums) == 2:
            return 1 if nums[1] == target else 0
        start_index = 0
        stop_index = len(nums) - 1
        while start_index < stop_index:
            mid = (start_index + stop_index) // 2
            if nums[mid] == target and mid+1 > len(nums)-1:
                return mid
            if nums[mid] == target and nums[mid + 1] != target:
                return mid
            if nums[mid] == target and nums[mid + 1] == target:
                start_index = mid+1
            elif nums[mid] > target:
                stop_index = mid - 1
            elif nums[mid] < target:
                start_index = mid+1
            else:
                return None
        if nums[stop_index] != target:
            return -1
        return stop_index