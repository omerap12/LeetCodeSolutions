# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        using backtrack calculate all parentheses, then check if it's valid -> if so add to answer.
        """
        answer = []
        brackets = ["(", ")"]
        tmp_string = ""
        self.backtrack(answer, brackets, tmp_string, n)
        return answer

    def backtrack(self, answer, brackets, tmp_string, n):
        if len(tmp_string) == n * 2:
            if self.isValid(tmp_string):
                answer.append(tmp_string)
        else:
            for i in range(len(brackets)):
                if len(tmp_string) < n*2:
                    tmp_string += brackets[i]
                    self.backtrack(answer, brackets, tmp_string, n)
                    tmp_string = tmp_string[0:len(tmp_string) - 1]

    def isValid(self, s):
        valid_parentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        for word in s:
            if word in valid_parentheses.keys():
                if stack and stack[-1] == valid_parentheses[word]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(word)
        if len(stack) == 0:
            return True
        return False
