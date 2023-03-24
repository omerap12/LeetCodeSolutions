# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        The idea is to merge intervals that intersect each other into the smallest interval that intersects them.
        For example for the intervals: [1,5],[4,8] We will create an interval [4,5]
        This will be done for all the intervals and we will return the size of all of them.
        (an interval that cannot be merged, we will continue and of course count it)
        """
        points.sort()
        merged_points = []
        start_interval = points.pop(0)
        while points:
            second_interval = points.pop(0)
            if start_interval[0] <= second_interval[0] <= start_interval[1] or \
                    start_interval[0] <= second_interval[0] <= start_interval[1]:
                start_interval = [max(start_interval[0], second_interval[0]),
                                  min(start_interval[1], second_interval[1])]
            else:
                merged_points.append(start_interval)
                start_interval = second_interval
        return len(merged_points)+1