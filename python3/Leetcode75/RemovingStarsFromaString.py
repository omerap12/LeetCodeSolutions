# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter == '*':
                stack.pop()
            else:
                stack.append(letter)
        return "".join(l for l in stack)