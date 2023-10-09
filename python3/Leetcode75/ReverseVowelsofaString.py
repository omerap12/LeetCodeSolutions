# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        ret = ""
        index_to_vowles = {}
        index = 0
        vowles = ('e','E','a','A','i','I','o','O','u','U')
        for word in s:
            if word in vowles:
                index_to_vowles[index] = word
                index += 1
        

        curr = index - 1
        for i in range(len(s)):
            if s[i] not in vowles:
                ret += s[i]
            else:
                ret += index_to_vowles[curr]
                curr -= 1 
        return ret



        