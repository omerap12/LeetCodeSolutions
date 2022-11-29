# Solution To: https://leetcode.com/problems/set-matrix-zeroes/submissions/

class Solution(object):
    def __init__(self):
        self.positions = []

    def setZeroes(self, matrix):
        row_length = len(matrix)
        column_length = len(matrix[0])

        # add position to the list of zero value positions.
        for i in range(row_length):
            for j in range(column_length):
                if matrix[i][j] == 0:
                    self.positions.append((i, j))

        # start working on the matrix
        for pair in self.positions:
            # set row to zero
            for i in range(column_length):
                matrix[pair[0]][i] = 0
            # set column to zero
            for j in range(row_length):
                matrix[j][pair[1]] = 0
        return matrix
