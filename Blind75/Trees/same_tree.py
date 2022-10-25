# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and not q or q and not p or p.val != q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)


root1 = TreeNode(1, TreeNode(2))
root2 = TreeNode(1, None, TreeNode(2))
root3 = TreeNode(1, TreeNode(2))

n = Solution()
print(n.isSameTree(root1,root3))
