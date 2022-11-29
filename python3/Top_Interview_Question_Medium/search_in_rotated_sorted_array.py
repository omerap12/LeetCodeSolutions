# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1
        k = self.get_index(nums)
        first_check = self.binarySearch(nums[k:len(nums)],target)
        if first_check == -1:
            second_check = self.binarySearch(nums[0:k+1],target)
            if second_check == -1:
                return -1
            return second_check
        return first_check+k

    def binarySearch(self,arr, target):
        lo = 0
        hi = len(arr) - 1
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if arr[lo] == target:
            return lo
        elif arr[hi] == target:
            return hi
        else:
            return -1

    def get_index(self, nums):
        stop_index = len(nums) - 1
        start_index = 0
        if nums[stop_index] >= nums[start_index]:
            return start_index
        while stop_index - start_index >= 1:
            mid = (start_index + stop_index) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid - 1] > nums[mid]:
                return mid
            if nums[mid] > nums[stop_index]:
                start_index = mid + 1
            else:
                stop_index = mid