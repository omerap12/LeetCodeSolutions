# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
    def __init__(self):
        self.answer = []

    def inorderTraversal(self, root):
        if root is not None:
            if root.left is not None:
                self.inorderTraversal(root.left)
            self.answer.append(root.val)
            if root.right is not None:
                self.inorderTraversal(root.right)
        return self.answer