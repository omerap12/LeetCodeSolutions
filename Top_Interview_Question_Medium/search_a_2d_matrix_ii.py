# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution(object):
    def searchMatrix(self, matrix, target):
        row_index = len(matrix) - 1
        column_index = 0
        while 0 <= row_index and column_index < len(matrix[0]):
            number = matrix[row_index][column_index]
            if number == target:
                return True
            elif number < target:
                column_index += 1
            else:
                row_index -= 1
        return False
