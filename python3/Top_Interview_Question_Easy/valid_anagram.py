# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        t_dict = {}
        for word in s:
            if word in s_dict.keys():
                s_dict[word] += 1
            else:
                s_dict[word] = 1
        for word in t:
            if word in t_dict.keys():
                t_dict[word] += 1
            else:
                t_dict[word] = 1
        return s_dict == t_dict
