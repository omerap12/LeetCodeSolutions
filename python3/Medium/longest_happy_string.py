# https://leetcode.com/problems/longest-happy-string/description/
from typing import List, Set


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Greedy algorithm: select the letter with the highest value first. if you can't select the letter with the
        highest value, select the second one and so on.
        """
        res = ""
        dict_letters = {0: "a", 1: "b", 2: "c"}
        arr_times = [0, 0, 0]
        arr = [a, b, c]
        while arr[0] != 0 or arr[1] != 0 or arr[2] != 0:
            max_indexes = self.get_max_index(arr)
            times_chose = float('inf')
            chosen_number = None
            for index in max_indexes:
                if arr_times[index] < times_chose:
                    chosen_number = index
                    times_chose = arr_times[index]
            if times_chose < 2 and arr[chosen_number] > 0:
                arr_times[chosen_number] += 1
                arr[chosen_number] -= 1
                res += dict_letters[chosen_number]
                for i in range(3):
                    if i != chosen_number:
                        arr_times[i] = 0
                continue

            second_indexes = self.get_second_max_index(arr)
            times_chose = float('inf')
            chosen_number = None
            for index in second_indexes:
                if arr_times[index] < times_chose:
                    chosen_number = index
                    times_chose = arr_times[index]
            if times_chose < 2 and arr[chosen_number] > 0:
                arr_times[chosen_number] += 1
                res += dict_letters[chosen_number]
                arr[chosen_number] -= 1
                for i in range(3):
                    if i != chosen_number:
                        arr_times[i] = 0
                continue

            third_indexes = self.get_third_max_index(arr)
            times_chose = float('inf')
            chosen_number = None
            for index in third_indexes:
                if arr_times[index] < times_chose:
                    chosen_number = index
                    times_chose = arr_times[index]
            if times_chose < 2 and arr[chosen_number] > 0:
                arr_times[chosen_number] += 1
                res += dict_letters[chosen_number]
                arr[chosen_number] -= 1
                for i in range(3):
                    if i != chosen_number:
                        arr_times[i] = 0
            else:
                return res
        return res

    def get_max_index(self, arr: List[int]) -> set[int]:
        max_number = max(arr)
        res = set()
        for i in range(len(arr)):
            if arr[i] == max_number:
                res.add(i)
        return res

    def get_second_max_index(self, arr: List[int]) -> set[int]:
        second_max_number = sorted(arr)[-2]
        res = set()
        for i in range(len(arr)):
            if arr[i] == second_max_number:
                res.add(i)
        return res

    def get_third_max_index(self, arr: List[int]) -> set[int]:
        third_max_number = min(arr)
        res = set()
        for i in range(len(arr)):
            if arr[i] == third_max_number:
                res.add(i)
        return res