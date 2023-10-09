# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ""
        min_word = min(len(word1),len(word2))
        max_word = max(len(word1),len(word2))
        for i in range(min_word):
            ret += word1[i]
            ret += word2[i]
        if len(word1) == max_word:
            ret += word1[min_word:]
        else:
            ret += word2[min_word:]
        return ret