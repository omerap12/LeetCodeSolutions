# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        matrix = []
        zero_line = [0]*len(colsum)
        matrix.append(zero_line.copy())
        matrix.append(zero_line.copy())
        if sum(colsum) < upper + lower:
            return []
        for column in range(len(colsum)):
            if colsum[column] == 2:
                matrix[1][column] = 1
                lower -= 1
                matrix[0][column] = 1
                upper -= 1
        if lower < 0 or upper < 0:
            return []
        for column in range(len(colsum)):
            if colsum[column] == 1:
                if lower == 0:
                    matrix[0][column] = 1
                    upper -= 1
                elif upper == 0:
                    matrix[1][column] = 1
                    lower -= 1
                elif lower < upper:
                    matrix[1][column] = 1
                    lower -= 1
                else:
                    matrix[0][column] = 1
                    upper -= 1
        if lower < 0 or upper < 0:
            return []
        return matrix