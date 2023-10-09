# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        words_splitted = s.split(' ')
        ret = " ".join(word for word in words_splitted[::-1] if word != "" and word != " ")
        return ret