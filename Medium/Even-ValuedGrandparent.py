# solution To: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.values = []

    def sumEvenGrandparent(self, root):
        self.values.clear()  # clear list from previous calculation
        self.helper(root, None, None)
        return sum(self.values)

    def helper(self, edge, currentFather, currentGrandParentValue):
        if currentGrandParentValue is not None:
            if currentGrandParentValue % 2 == 0:
                self.values.append(edge.val)  # add the value to the list
        if edge.left is not None:  # go left
            # set father value to grandparent value, set current edge as father value
            self.helper(edge.left, edge.val, currentFather)
        if edge.right is not None:
            # set father value to grandparent value, set current edge as father value
            self.helper(edge.right, edge.val, currentFather)


# basic test
root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1, TreeNode(4)))),
                TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
n = Solution()
print(n.sumEvenGrandparent(root)) # 18
