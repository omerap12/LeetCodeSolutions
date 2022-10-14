# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        indexes_to_ignore = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 or (i, j) in indexes_to_ignore:
                    continue
                self.set_column_and_row_to_zero(indexes_to_ignore, matrix, i, j)

    def set_column_and_row_to_zero(self, indexes_to_ignore, matrix, row, coloumn):
        for j in range(len(matrix[0])):
            if matrix[row][j] != 0:
                indexes_to_ignore.add((row, j))
            matrix[row][j] = 0

        for i in range(len(matrix)):
            if matrix[i][coloumn] != 0:
                indexes_to_ignore.add((i, coloumn))
            matrix[i][coloumn] = 0
