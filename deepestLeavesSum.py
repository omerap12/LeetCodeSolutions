class Solution(object):
    def deepestLeavesSum(self, root):
        deepest = self.halper(root)
        return self.answer(root, 0, deepest)

    def halper(self, root):
        if root is None:
            return 0
        return max(self.halper(root.left) + 1, self.halper(root.right) + 1)

    def answer(self, root, current, maxDepth):
        if root is None:
            return 0
        if root.left is None and root.right is None and current == maxDepth:
            return root.val
        return self.answer(root.left, current + 1, maxDepth) + self.answer(root.right, current + 1, maxDepth)
