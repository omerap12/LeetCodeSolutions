solution To: https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.rstrip()
        count = 0
        if s == "":
            return count

        for i in range(len(word) - 1, -1, -1):
            if word[i] == " ":
                return count
            count += 1
        return count
