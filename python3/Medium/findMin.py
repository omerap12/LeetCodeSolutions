solution To: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, numbers, low_index, high_index):
        if low_index > high_index:
            return numbers[0]
        if low_index == high_index:
            return numbers[high_index]

        middle_index = int((low_index + high_index) / 2)

        # for array like this [4,5,6,7,0,1,2]
        if numbers[middle_index] > numbers[middle_index + 1] and middle_index < high_index:
            return numbers[middle_index + 1]
        # for array like this [10,1,2,5]
        if numbers[middle_index] < numbers[middle_index - 1] and low_index < middle_index:
            return numbers[middle_index]

        # get to the left side of the array
        if numbers[high_index] > numbers[middle_index]:
            return self.helper(numbers, 0, middle_index - 1)

        # get the right side of the array
        else:
            return self.helper(numbers, middle_index + 1, high_index)
