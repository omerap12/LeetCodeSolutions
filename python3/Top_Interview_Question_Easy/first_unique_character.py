# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        dict_words = {}
        set_words = set()
        used_letters = {}
        for i in range(len(s)-1,-1,-1):
            dict_words[i] = set_words.copy()
            set_words.add(s[i])
        for index in range(len(s)):
            if s[index] in used_letters.keys():
                continue
            if s[index] not in dict_words[index]:
                return index
            used_letters[s[index]] = 1
        return -1
