# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        dict_values = {}
        self.helper(root,dict_values,0)
        res = []
        for key in dict_values.keys():
            res.append(max(dict_values[key]))
        return res

    def helper(self,root,dict_values,height):
        if root:
            if height in dict_values.keys():
                dict_values[height].append(root.val)
            else:
                dict_values[height] = [root.val]
            self.helper(root.left,dict_values,height+1)
            self.helper(root.right,dict_values,height+1)

n = Solution()
root = TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)),TreeNode(2,None,TreeNode(9)))
print(n.largestValues(root))
