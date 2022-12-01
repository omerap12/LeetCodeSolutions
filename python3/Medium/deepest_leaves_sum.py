# https://leetcode.com/problems/deepest-leaves-sum/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Keep both the maximum level and the maximum val
    """
    def __init__(self):
        self.max_sum = 0
        self.max_level = 0

    def deepestLeavesSum(self, root):
        self.helper(root, 0)
        return self.max_sum

    def helper(self, root, level):
        if level == self.max_level:
            self.max_sum += root.val
        if level > self.max_level:
            self.max_sum = root.val
            self.max_level = level
        if root.left:
            self.helper(root.left, level + 1)
        if root.right:
            self.helper(root.right, level + 1)


root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
n = Solution()
print(n.deepestLeavesSum(root))
