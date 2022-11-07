Solution To: https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        column_length = len(matrix[0]) - 1  # get the columns number
        row_length = len(matrix) - 1  # get the rows number
        return self.find_element(matrix, row_length, column_length, target)  # call aux function

    def find_element(self, matrix, i, j, target):
        """
        function that search for specific number in matrix, starting from the end to the start
        :param matrix: the matrix given
        :param i: rows number
        :param j: columns number
        :param target: number to search
        :return: True\False
        """
        if i == 0 and j == 0:  # if were at the start, last check
            return matrix[i][j] == target

        if matrix[i][j] == target:  # if the current matrix index is the target return True
            return True

        if matrix[i][j] < target:  # for one row matrix
            return False

        if matrix[i][j] > target and i == 0:  # if the current index is larger than target and were on the first row, 
            # go left 
            return self.find_element(matrix, i, j - 1, target)

        if matrix[i - 1][j] > target:  # if the upper index is bigger than target go recursively there
            return self.find_element(matrix, i - 1, j, target)
        if matrix[i - 1][j] < target and j == 0:  # if the current index is smaller than target and were on the first 
            # column, go up 
            return self.find_element(matrix, i - 1, j, target)
        if matrix[i - 1][j] < target:  # if the current index is smaller than target, go left 
            return self.find_element(matrix, i, j - 1, target)
        if matrix[i - 1][j] == target: # if upper index is the number return True
            return True
