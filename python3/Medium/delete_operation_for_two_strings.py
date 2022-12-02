# https://leetcode.com/problems/delete-operation-for-two-strings/description/
class Solution:
    def minDistance(self, word1, word2):
        """
        using DP, create a 2d matrix with row as word1 letters and columns as word2 letters
        dp[i][j] is the number of moves to set word1 == word2
        Set the first row with the number of the letters at the i index of word 1
        Set first column with the number of the letters at the i index of word 2
        if word1[i] == word2[j] -> ignore the last to chars of the words -> = dp[i-1][j-1]
        else take the minimum between remove the last char of word1 and remove the last char of word2
        """
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for row in range(len(dp)):
            for column in range(len(dp[0])):
                if row == 0 and column == 0:
                    dp[row][column] = 0
                elif row == 0:
                    dp[row][column] = column
                elif column == 0:
                    dp[row][column] = row
                else:
                    if word1[row - 1] == word2[column - 1]:
                        dp[row][column] = dp[row - 1][column - 1]
                    else:
                        dp[row][column] = min(dp[row - 1][column], dp[row][column - 1]) + 1
        return dp[-1][-1]
