# https://leetcode.com/problems/detonate-the-maximum-bombs/solutions/
import math


class Solution:
    def maximumDetonation(self, bombs):
        """
        Set the bombs as nodes in graph.
        x -> y if bomb_x denote bomb_y
        return max unique nodes of path start with bomb a
        """
        bombs_neighbors = {}
        for i in range(len(bombs)):
            bombs_neighbors[i] = self.get_neighbers(i, bombs)
        res = 0
        for i in range(len(bombs)):
            res = max(res, self.bfs(bombs_neighbors, i))
        return res

    def get_neighbers(self, bomb_index, bombs):
        neighbors = []
        for i in range(len(bombs)):
            if i == bomb_index:
                continue
            if self.is_intersect(bombs[bomb_index], bombs[i]):
                neighbors.append(i)
        return neighbors

    def is_intersect(self, bomb_a, bomb_b):
        x1 = bomb_a[0]
        y1 = bomb_a[1]
        r1 = bomb_a[2]
        x2 = bomb_b[0]
        y2 = bomb_b[1]
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d <= r1

    def bfs(self, neighbors_list, starting_bomb):
        visited = set()
        visited.add(starting_bomb)
        stack = [starting_bomb]
        while stack:
            neighbors = neighbors_list[stack.pop()]
            for bomb in neighbors:
                if bomb not in visited:
                    visited.add(bomb)
                    stack.append(bomb)
        return len(visited)
