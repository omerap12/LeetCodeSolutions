# https://leetcode.com/problems/number-of-islands/description/
from typing import List


class Solution:
    """
    Start with index 1 and spread out using dfs.
    for each dfs traversal save the node in set (to avoid loops).
    travers until as long as there is a route with index 1, when finish up counter by one.
    """
    def __init__(self):
        self.seen = set()
        self.grid = None

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.grid = grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row, column) in self.seen or self.grid[row][column] == "0":
                    continue
                else:
                    self.dfs(row, column)
                    res += 1
        return res

    def dfs(self, x, y):
        if (x, y) in self.seen:
            return
        self.seen.add((x, y))
        # move right
        if y + 1 < len(self.grid[0]) and self.grid[x][y + 1] == "1":
            self.dfs(x, y + 1)
        # move left
        if y - 1 > -1 and self.grid[x][y - 1] == "1":
            self.dfs(x, y - 1)
        # move down
        if x + 1 < len(self.grid) and self.grid[x + 1][y] == "1":
            self.dfs(x + 1, y)
        # move up
        if x - 1 > -1 and self.grid[x - 1][y] == "1":
            self.dfs(x - 1, y)


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid3 = [["1", "1", "1"],
         ["0", "1", "0"],
         ["1", "1", "1"]]
n = Solution()
print(n.numIslands(grid2))
