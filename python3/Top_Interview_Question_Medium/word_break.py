# https://leetcode.com/problems/word-break/
class Solution(object):
    """
    Google interview question!
    a classic dp question.
    The key is to start from the end of the string backwards, if from index i there is a word a set the index of the 
    dp array to value of the index i + length of the word it's match.
    The last index of the dp is true and the final answer will be at 0 index.
    """

    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
        return dp[0]