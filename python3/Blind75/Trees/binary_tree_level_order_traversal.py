# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        dict_counter = {}
        dict_counter[root] = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
                dict_counter[node.left] = dict_counter[node] + 1
            if node.right:
                stack.append(node.right)
                dict_counter[node.right] = dict_counter[node] + 1
        levels = max(dict_counter.values())
        answer = []
        for i in range(levels+1):
            answer.append([])
        for key, value in dict_counter.items():
            answer[value].append(key.val)
        return answer

n = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(n.levelOrder(root))

