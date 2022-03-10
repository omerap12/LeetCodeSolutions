#Solution to: https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
    def minPathSum(self, grid):
        rows = len(grid)
        columns = len(grid[0])

        # fill the matrix row by row - answer in grid[rows-1][columns-1]
        for i in range(rows):
            for j in range(columns):
              # first entry
                if i == 0 and j == 0:
                    continue
              # first row, just one option - go left
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
              # first column, just one option - go down
                elif j==0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                  # take the min between left and down
                    grid[i][j] = grid[i][j] + min(grid[i][j-1],grid[i-1][j])
        return grid[rows-1][columns-1]
