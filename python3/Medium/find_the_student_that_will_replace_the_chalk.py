# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk, k):
        sum_chalk = sum(chalk)

        left = k % sum_chalk
        if left == 0:
            return 0
        for i in range(len(chalk)):
            if left - chalk[i] < 0:
                return i
            left -= chalk[i]
