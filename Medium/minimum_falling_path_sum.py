# https://leetcode.com/problems/minimum-falling-path-sum/description/

class Solution:
    def minFallingPathSum(self, matrix):
        """
        for each row calculate the min between row-1 and column-1 , row-1 and column, row-1 and column+1 
        which are the exact falling paths that available.
        the answer will be the min in the last arr
        """
        line = [float('inf')] * len(matrix[0])
        dp = []
        dp.append(matrix[0].copy())
        for i in range(1,len(matrix),1):
            dp.append(line.copy())
        # building the matrix except the first row
        for row in range(1, len(matrix), 1):
            for column in range(len(matrix[0])):
                if column == 0:
                    dp[row][column] = matrix[row][column] + min(dp[row - 1][column], dp[row - 1][column + 1])
                elif column == len(matrix[0]) - 1:
                    dp[row][column] = matrix[row][column] + min(dp[row - 1][column - 1], dp[row - 1][column])
                else:
                    dp[row][column] = matrix[row][column] + min(dp[row - 1][column - 1], dp[row - 1][column],
                                                                dp[row - 1][column + 1])
        return min(dp[len(matrix)-1])


n = Solution()
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(matrix)
print(n.minFallingPathSum(matrix))

