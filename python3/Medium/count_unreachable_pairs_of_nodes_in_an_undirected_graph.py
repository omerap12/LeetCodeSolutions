# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
from typing import List


class Solution:
    """
    For n nodes the maximum number of pairs is according the formula n * (n - 1) // 2
    The key is to find the number of nodes of each node in scc graph and count its pairs using the formula.
    The number of missing pairs is the subtraction of the maximum pairs minus the sum of pairs in scc
    """
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        nodes_counter = []
        neighbor_list = {i: [] for i in range(n)}
        visited = set()
        for e in edges:
            neighbor_list[e[0]].append(e[1])
            neighbor_list[e[1]].append(e[0])
        for node in range(n):
            counter = 0
            if node in visited:
                continue
            stack = [node]
            while stack:
                counter += 1
                cur = stack.pop()
                visited.add(cur)
                for neighbor in neighbor_list[cur]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
            nodes_counter.append(counter)
        pairs_connected = 0
        for c in nodes_counter:
            pairs_connected += self.count_pairs(c)
        return self.count_pairs(n) - pairs_connected

    def count_pairs(self, n):
        return n * (n - 1) // 2


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
# n = 314
# edges =3
sol = Solution()
print(sol.countPairs(n, edges))
