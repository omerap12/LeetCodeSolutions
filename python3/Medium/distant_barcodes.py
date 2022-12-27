# https://leetcode.com/problems/distant-barcodes/description/
from typing import List
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
         choose the max available choice, do it by using max_heap.
         take the 2 max values each time add them ro res, update the heap.
         if value becomes 0 do not return it to the heap.
         do it until numbers available in the heap.
        """
        res = []
        number_counter = {}
        for number in barcodes:
            if number in number_counter.keys():
                number_counter[number] += 1
            else:
                number_counter[number] = 1

        max_heap = []
        for key, val in number_counter.items():
            max_heap.append((-val, key))
        heapq.heapify(max_heap)

        while max_heap:
            number_of_occurrences, key = heapq.heappop(max_heap)
            res.append(key)
            number_of_occurrences += 1
            number_of_occurrences_2, key_2 = None, None
            if max_heap:
                number_of_occurrences_2, key_2 = heapq.heappop(max_heap)
                res.append(key_2)
                number_of_occurrences_2 += 1
            if number_of_occurrences != 0:
                heapq.heappush(max_heap,(number_of_occurrences, key))
            if number_of_occurrences_2 != 0 and number_of_occurrences_2 is not None:
                heapq.heappush(max_heap,(number_of_occurrences_2, key_2))
        return res
