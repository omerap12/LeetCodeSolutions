# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        The idea is to run BFS from node1 and node2 and take node v, which the maximum distance between node1 to v
        and node2 to v is minimal if there is no such node we return -1
        """
        neighbors = {}
        for i in range(len(edges)):
            if edges[i] != -1:
                neighbors[i] = edges[i]
        ssp_node_1 = self.bfs(node1, neighbors)
        ssp_node_2 = self.bfs(node2, neighbors)
        ret = []
        min_distance = float('inf')
        for key, value in ssp_node_1.items():
            if key not in ssp_node_2:
                continue
            if max(ssp_node_2[key], value) == min_distance:
                ret.append(key)
            elif max(ssp_node_2[key], value) < min_distance:
                ret = [key]
                min_distance = max(ssp_node_2[key], value)
        if ret:
            return min(ret)
        return -1

    def bfs(self, start, neighbors_list: dict[int]) -> dict[int]:
        visited = {start}
        stack = [start]
        distances = {start: 0}
        while stack:
            curr = stack.pop()
            if curr not in neighbors_list.keys():
                continue
            next_vertex = neighbors_list[curr]
            if next_vertex not in visited:
                visited.add(next_vertex)
                distances[next_vertex] = distances[curr] + 1
                stack.append(next_vertex)
        return distances
