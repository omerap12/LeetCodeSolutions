# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Just solve using simple dfs, for every letter in the word save its index on the board (i,j)
        Then using dfs from the first letter see if you can reach the last letter.
        :param board: board input where board[i][j] = letter.
        :param word: word to fine.
        :return: True if you can create the word from the board.
        """
        words_dict = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word:
                    if board[i][j] in words_dict.keys():
                        words_dict[board[i][j]].append((i, j))
                    else:
                        words_dict[board[i][j]] = [(i, j)]
        if len(words_dict) != len(set(word)):
            return False

        # DFS
        for start_index in words_dict[word[0]]:
            if self.dfs(start_index, word, words_dict, 0, set()):
                return True
        return False

    def dfs(self, current_location: tuple, word: str, words_dict: dict, counter: int, visited: set) -> bool:
        # You reach the final letter so return True
        if counter == len(word) - 1:
            return True
        # add the current location to visited to avoid loops
        visited.add(current_location)
        # get the next letter indexes
        next_letter_indexes = words_dict[word[counter + 1]]
        first, second, third, fourth = False, False, False, False
        # check if you can move right left up or down
        if (current_location[0] + 1, current_location[1]) in next_letter_indexes and (
        current_location[0] + 1, current_location[1]) not in visited:
            first = self.dfs((current_location[0] + 1, current_location[1]), word, words_dict, counter + 1,
                             visited.copy())
        if (current_location[0] - 1, current_location[1]) in next_letter_indexes and (
        current_location[0] - 1, current_location[1]) not in visited:
            second = self.dfs((current_location[0] - 1, current_location[1]), word, words_dict, counter + 1,
                              visited.copy())
        if (current_location[0], current_location[1] + 1) in next_letter_indexes and (
        current_location[0], current_location[1] + 1) not in visited:
            third = self.dfs((current_location[0], current_location[1] + 1), word, words_dict, counter + 1,
                             visited.copy())
        if (current_location[0], current_location[1] - 1) in next_letter_indexes and (
        current_location[0], current_location[1] - 1) not in visited:
            fourth = self.dfs((current_location[0], current_location[1] - 1), word, words_dict, counter + 1,
                              visited.copy())
        return False or first or second or third or fourth
