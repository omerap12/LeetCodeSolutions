# https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        # create the matrix, answer will be in dynamic_array[m-1][n-1]
        dynamic_array = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            for column in range(n):
                if row == 0 and column == 0:
                    dynamic_array[row][column] = 1
                elif row == 0:
                    dynamic_array[row][column] = dynamic_array[row][column-1]
                elif column == 0:
                    dynamic_array[row][column] = dynamic_array[row-1][column]
                else:
                    dynamic_array[row][column] = dynamic_array[row-1][column] + dynamic_array[row][column-1]
        return dynamic_array[m-1][n-1]
