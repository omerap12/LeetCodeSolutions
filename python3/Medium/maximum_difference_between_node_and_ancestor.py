# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        For each subtree we save the following information:
        * Maximum node val (till now)
        * Minimum node val (till now)
        * Max difference val (till now)
        When we encounter new node, we calculate the node difference value and send to its sons the information.
        """
        left, right = 0, 0
        # Go left subtree from root. max_val,min_val are init as the root val. max_diff is 0
        if root.left:
            left = max(left, self.helper(root.left, root.val, root.val, 0))
        # Go right subtree from root. max_val,min_val are init as the root val. max_diff is 0
        if root.right:
            right = max(right, self.helper(root.right, root.val, root.val, 0))
        return max(left, right)

    def helper(self, root, max_til_now, min_til_now, max_diff):
        """
        Helper function, do the things I explained above.
        """

        # Calculate the max diff till now
        max_diff = max(max_diff, abs(root.val - max_til_now), abs(min_til_now - root.val))
        r, l = 0, 0
        # Go right subtree
        if root.right:
            r = self.helper(root.right, max(max_til_now, root.val), min(root.val, min_til_now), max_diff)
        # Go left subtree
        if root.left:
            l = self.helper(root.left, max(max_til_now, root.val), min(root.val, min_til_now), max_diff)
        # return its max value
        return max(max_diff, l, r)
