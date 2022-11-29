# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        calculating the sum of every iteration.
        setting two pointers - one at the begging and one at the end.
        advanced the pointer which its height is lower 
        """
        if len(height) == 0 or len(height) == 1:
            return 0
        right_pointer = len(height)-1
        left_pointer = 0
        area_max = 0
        while right_pointer != left_pointer and left_pointer >= 0 and right_pointer < len(height):
            area_max = max(area_max, (right_pointer - left_pointer) * min(height[right_pointer], height[left_pointer]))
            if height[right_pointer] > height[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return area_max
