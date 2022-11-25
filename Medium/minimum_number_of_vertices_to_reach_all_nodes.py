class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        res = []
        neighboors = {v: [] for v in range(n)}
        nodes_degree_in = {v: 0 for v in range(n)}
        for e in edges:
            neighboors[e[0]].append(e[1])
            nodes_degree_in[e[1]] += 1
        for key, val in nodes_degree_in.items():
            if val == 0:
                res.append(key)
        return res