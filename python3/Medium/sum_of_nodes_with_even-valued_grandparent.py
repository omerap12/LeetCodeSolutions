# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root, None, None)

    def helper(self, root: TreeNode, parent: TreeNode, grandparent: TreeNode) -> int:
        value = 0
        if grandparent is not None and grandparent.val % 2 == 0:
            value += root.val
        if root.left:
            value += self.helper(root.left, root, parent)
        if root.right:
            value += self.helper(root.right, root, parent)
        return value

