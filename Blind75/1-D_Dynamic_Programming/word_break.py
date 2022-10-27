#  https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            if dp[i]:
                continue
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
        return dp[0]

