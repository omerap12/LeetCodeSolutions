# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/
from typing import List


class Solution:
	def containsCycle(self, grid: List[List[str]]) -> bool:
		"""
		Circle in a grid -> we use dfs.
		Check if right,left,up,down if we can go there (same letter as the current index) and check it's not the last
		index I visited. if so go there. if found circle return True else False
		:param grid: List[List[str]]
		:return: if found circle return True else False
		"""
		used_boxes = set()
		for row in range(len(grid)):
			for column in range(len(grid[0])):
				if (row, column) in used_boxes:
					continue
				if self.dfs((row, column), grid, set(), None, grid[row][column],used_boxes):
					return True
		return False

	def dfs(self, start: tuple, grid: List[List[str]], visited: set, last_visited: tuple, letter: str,used_boxes:set):
		"""
		The dfs method. check all sides that is the same letter as current and not last visited.
		:param start: the current index
		:param grid:  List[List[str]]
		:param visited: all nodes we traversed
		:param last_visited: the last node we visited
		:param letter: the letter of the current index
		:param used_boxes: for not starting the dfs from nodes we already have been traversed
		:return: if found circle return True else False
		"""
		if start in visited and start != last_visited:
			return True
		visited.add(start)
		used_boxes.add(start)
		if start[0] - 1 > -1 and grid[start[0] - 1][start[1]] == letter and (start[0] - 1, start[1]) != last_visited:
			if self.dfs((start[0] - 1, start[1]), grid, visited, start, letter,used_boxes):
				return True
		if start[0] + 1 < len(grid) and grid[start[0] + 1][start[1]] == letter and (start[0] + 1, start[1]) != last_visited:
			if self.dfs((start[0] + 1, start[1]), grid, visited, start, letter,used_boxes):
				return True

		if start[1] + 1 < len(grid[0]) and grid[start[0]][start[1] + 1] == letter and (start[0], start[1]+1) != last_visited:
			if self.dfs((start[0], start[1] + 1), grid, visited, start, letter,used_boxes):
				return True
		if start[1] - 1 > -1 and grid[start[0]][start[1] - 1] == letter and (start[0], start[1]-1) != last_visited:
			if self.dfs((start[0], start[1] - 1), grid, visited, start, letter,used_boxes):
				return True
		return False
