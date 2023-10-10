# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        rows,colums = [],[]
        for row in grid:
            rows.append(row)
        tmp = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp.append(grid[j][i])
            colums.append(tmp.copy())
            tmp.clear()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rows[i] == colums[j]:
                    ret += 1
        return ret