# https://leetcode.com/problems/rotate-image/
class Solution(object):
    """
    Microsoft interview question!
    General approach:
    * set boundaries (left,right,top,bottom) (left < right : stop algorithm if not)
    * rotating the matrix from the outside layer to the inner layer - for the outermost layer rotating the first row,
    for the inside layer -> sub-problem , shift pointers by one (left+1,right-1,top-1,bottom+1)
    * save the offset for every number in the martix
    * Do the rotating in reversed order , take the front element and put it on the current index. one tmp variable needed
    """

    def rotate(self, matrix):
        # initiliaze of the pointers
        left = 0
        right = len(matrix) - 1
        while left < right:
            # iterate entire row except last element (because the first one make the rotation with it)
            # i is the offset of every pointer
            for i in range(right-left):
                bottom = right
                top = left
                """
                make the rotation, reverse order
                """

                # get the left,top in a temp variable
                # it's the first tow
                tmp = matrix[top][left+i]

                # moving the bottom left to the top right
                matrix[top][left+i] = matrix[bottom-i][left]

                # moving the bottom right to the bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # moving the top right to the bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                # moving the temp to the top right
                matrix[top+i][right] = tmp

            # moving the next index of the line
            left += 1
            right -= 1
