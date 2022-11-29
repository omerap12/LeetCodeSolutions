# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        while root:
            if root.val > max_val:  # p, q belong to the left subtree
                root = root.left
            elif root.val < min_val:  # p, q belong to the right subtree
                root = root.right
            else:  # Now, min_val <= root.val <= max_val -> This is the LCA between p and q
                return root
        return None
