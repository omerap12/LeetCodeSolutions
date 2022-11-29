# https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        Perform binary search on the range and not on the input array
        """
        if len(nums) % 2 == 0:
            start_index = 1
        else:
            start_index = 0
        stop_index = len(nums) - 1
        if nums.count(stop_index) > 1:
            return stop_index
        while start_index < stop_index:
            mid = int(start_index + stop_index) // 2
            if nums.count(mid) > 1:
                return mid
            count_small_than_mid = 0
            count_bigger_than_mid = 0
            for number in nums:
                if start_index <= number < mid:
                    count_small_than_mid += 1
                elif mid <= number < stop_index:
                    count_bigger_than_mid += 1
            if count_small_than_mid < count_bigger_than_mid:
                start_index = mid + 1
            else:
                stop_index = mid
