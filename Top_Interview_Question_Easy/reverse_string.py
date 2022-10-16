# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        mid = int(len(s) / 2)
        for i in range(mid):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp
