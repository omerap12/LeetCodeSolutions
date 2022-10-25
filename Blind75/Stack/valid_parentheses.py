# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        dict_parent = {"}": "{", "]": "[", ")": "("}
        stack = []
        for l in s:
            if l not in dict_parent.keys():
                stack.append(l)
            else:
                if stack:
                    closing = stack.pop()
                    if dict_parent[l] != closing:
                        return False
                else:
                    return False
        return len(stack) == 0
