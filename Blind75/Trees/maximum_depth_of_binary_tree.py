# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root:
            return self.helper(root,1)
        return 0
    def helper(self,root,level):
        if root.right and root.left:
            return max(self.helper(root.left,level+1),self.helper(root.right,level+1))
        elif root.right:
            return self.helper(root.right,level+1)
        elif root.left:
            return self.helper(root.left, level+1)
        else:
            return level


root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
n = Solution()
print(n.maxDepth(root))

