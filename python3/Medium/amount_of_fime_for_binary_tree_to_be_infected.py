# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    """
    The problem is just: what is the distance of the furthest node from start node?
    So we create a graph and running bfs.
    """
    def __init__(self):
        self.matrix = {}
        self.distances = {}

    def fill_matrix(self, root) -> None:
        if root.left:
            if root.val in self.matrix.keys():
                self.matrix[root.val].append(root.left.val)
            else:
                self.matrix[root.val] = [root.left.val]
            if root.left.val in self.matrix.keys():
                self.matrix[root.left.val].append(root.val)
            else:
                self.matrix[root.left.val] = [root.val]
            self.fill_matrix(root.left)
        if root.right:
            if root.val in self.matrix.keys():
                self.matrix[root.val].append(root.right.val)
            else:
                self.matrix[root.val] = [root.right.val]
            if root.right.val in self.matrix.keys():
                self.matrix[root.right.val].append(root.val)
            else:
                self.matrix[root.right.val] = [root.val]
            self.fill_matrix(root.right)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.fill_matrix(root)
        self.bfs(start)
        return max(self.distances.values())

    def bfs(self,start:int) -> None:
        stack = [start]
        self.distances[start] = 0
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            if curr not in self.matrix.keys():
                continue
            for v in self.matrix[curr]:
                if v in visited:
                    continue
                self.distances[v] = self.distances[curr] + 1
                stack.append(v)
