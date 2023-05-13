
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Simple solution: create a graph and use bfs from target node.
    """
    def __init__(self) -> None:
        self.neighbors = {}
        self.distances = {}
    
    def create_graph(self,root:TreeNode) -> None:
        """
        Check if node has left son and right son. add them to neighbor list and continue recursively.
        """
        if root.val not in self.neighbors.keys():
            self.neighbors[root.val] = []
        if root.left:
            if root.left.val not in self.neighbors.keys():
                self.neighbors[root.left.val] = []
            self.neighbors[root.left.val].append(root.val)
            self.neighbors[root.val].append(root.left.val)
            self.create_graph(root.left)
        if root.right:
            if root.right.val not in self.neighbors.keys():
                self.neighbors[root.right.val] = []
            self.neighbors[root.right.val].append(root.val)
            self.neighbors[root.val].append(root.right.val)
            self.create_graph(root.right)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Perform BFS. don't add nodes to the stack when distance is k and above.
        """
        self.create_graph(root)
        ret = []
        self.distances[target] = 0
        stack = [target]
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                for node_val in self.neighbors[current]:
                    if node_val in self.neighbors[node_val] or node_val in visited:
                        continue
                    distance_of_new_node = self.distances[current] + 1
                    self.distances[node_val] = distance_of_new_node
                    if distance_of_new_node < k:
                        stack.append(node_val)
                    if distance_of_new_node == k:
                        ret.append(node_val)
                visited.add(current)
        return ret


n = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(n.distanceK(root,5,3))