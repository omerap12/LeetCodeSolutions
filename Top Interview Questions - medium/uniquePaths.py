Solution To: https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :param m: rows number
        :param n: columns number
        :return: number of unique paths
        """
        dynamic_array = [[1 for i in range(n)] for j in range(m)]  # creating a 2d array with m rows and n columns,
        # initialize every index with start value of 1

        for row_number in range(1, m):  # iterating through the rows
            for column_number in range(1, n):  # iterating through the columns
                dynamic_array[row_number][column_number] = dynamic_array[row_number - 1][column_number] + \
                                                           dynamic_array[row_number][column_number - 1]
                # sum all path to specific index
        return dynamic_array[m - 1][n - 1]  # return the end index which is the answer
