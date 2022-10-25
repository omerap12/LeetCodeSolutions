# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        if root:
            new_root = TreeNode(root.val)
            self.copy_tree(root,new_root)
            return new_root
        return root

    def copy_tree(self,root,new_root):
        if root.right:
            new_root.left = TreeNode(root.right.val)
            self.copy_tree(root.right,new_root.left)
        if root.left:
            new_root.right = TreeNode(root.left.val)
            self.copy_tree(root.left,new_root.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
n = Solution()
new_root = n.invertTree(root)

