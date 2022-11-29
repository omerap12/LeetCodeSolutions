# https://leetcode.com/problems/unique-paths-ii/
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        row_number = len(obstacleGrid)
        column_number = len(obstacleGrid[0])
        dp = [[float('inf')] * column_number]
        for i in range(row_number-1):
            dp.append(dp[0].copy())

        for i in range(row_number):
            for j in range(column_number):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row_number-1][column_number-1]