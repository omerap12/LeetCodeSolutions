# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first_nodes,second_nodes = [],[]
        self.get_leaves(root1,first_nodes)
        self.get_leaves(root2,second_nodes)
        return first_nodes == second_nodes


    def get_leaves(self,root:TreeNode,l:list) -> list:
        if not root.left and not root.right:
            l.append(root.val)
        if root.left:
            self.get_leaves(root.left, l)
        if root.right:
            self.get_leaves(root.right, l)