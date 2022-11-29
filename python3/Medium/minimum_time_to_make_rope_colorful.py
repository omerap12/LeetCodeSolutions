# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    """
    Intuition: becuase you remove the min ballon value, check if baloon[i] = baloon[i+1] if so
    remove the min (and add it to res), set the next ballon price to be the max value between
    the two (cause you removed the min on)
    for example: 5,2,3
    remove 2, now we have 5 and 3 so the array should be 5,3
    """
    def minCost(self, colors, neededTime):
        res = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                res += min(neededTime[i],neededTime[i+1])
                neededTime[i+1] = max(neededTime[i+1],neededTime[i])
        return res