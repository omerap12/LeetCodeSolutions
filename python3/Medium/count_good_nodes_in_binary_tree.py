# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Save for each node the max node until reaching it (no need to save all the path)
    send to its sons the same function with the argument max(prev_node.val,current.val)
    """
    def __init__(self):
        self.counter = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root,root.val)
        return self.counter

    def helper(self, root, prev_node):
        if root.val >= prev_node:
            self.counter += 1
        if root.left:
            self.helper(root.left, max(prev_node,root.val))
        if root.right:
            self.helper(root.right, max(prev_node,node.val))
