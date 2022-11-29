# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        answer = []
        intervals.sort()
        answer.append(intervals[0])
        for i in range(1,len(intervals),1):
            if answer[-1][1] < intervals[i][0]:
                answer.append(intervals[i])
            else:
                answer[-1] = [min(answer[-1][0],intervals[i][0])
                        ,max(answer[-1][1],intervals[i][1])]
        return answer
