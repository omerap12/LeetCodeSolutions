# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        new_intervals = []
        for interval in intervals:
            if not new_intervals:
                new_intervals.append(interval)
            else:
                if interval[0]<=new_intervals[-1][1]:
                    new_intervals[-1] = [min(interval[0],new_intervals[-1][0]),
                                     max(interval[1],new_intervals[-1][1])]
                else:
                    new_intervals.append(interval)
        return new_intervals
