# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
from typing import List


class Solution:
    """
    First we need at least n-1 edges.
    The key is to find all connected component. we can find all of them using dfs algorithm.
    we count all the connected components. if we have 1 component we need nothing.
    if we have 2 components we need one edge to connect them.
    if we have 3 components we need two edges to connect them.
    .
    .
    so we return number_of_components - 1
    """
    def __init__(self):
        self.visited = set()
        self.nodes_list = {}

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        for i in range(n):
            self.nodes_list[i] = []
        for conn in connections:
            self.nodes_list[conn[0]].append(conn[1])
            self.nodes_list[conn[1]].append(conn[0])
        islands = 0
        empty_nodes = 0
        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                islands += 1
            if len(self.nodes_list[i]) == 0:
                empty_nodes += 1
        return islands-1

    def dfs(self, node):
        self.visited.add(node)
        for neighbor in self.nodes_list[node]:
            if neighbor in self.visited:
                continue
            self.dfs(neighbor)


sol = Solution()
n = 4
connections = [[0, 1], [0, 2], [1, 2]]
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(sol.makeConnected(n, connections))
