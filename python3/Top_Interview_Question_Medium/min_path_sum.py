# https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        row_number = len(grid)
        column_number = len(grid[0])
        dp = [[float('inf')] * column_number]
        for row in range(row_number - 1):
            dp.append(dp[0].copy())
        for i in range(row_number):
            for j in range(column_number):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i-1][j])
        return dp[row_number-1][column_number-1]