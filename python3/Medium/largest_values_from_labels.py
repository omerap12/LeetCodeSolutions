# https://leetcode.com/problems/largest-values-from-labels/description/
from typing import List
import heapq


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        """
        Greedy algorithm: Take the maximum value that you can.
        We create a map which maps label->number of times selected.
        For every item we encounter (using heappop) we checked if map[label] < useLimit, if so we add the value.
        Else we continue.
        We do this until number_of_items selected is equal to numWanted, or no elements left.
        """
        used_items = {}
        counter_items = 0
        ret = 0
        heap = [(-value, label) for value, label in zip(values, labels)]
        heapq.heapify(heap)
        while heap and counter_items < numWanted:
            value, label = heapq.heappop(heap)
            if label in used_items.keys() and used_items[label] < useLimit:
                ret += value
                counter_items += 1
                used_items[label] += 1
            elif label in used_items.keys() and used_items[label] >= useLimit:
                continue
            else:
                used_items[label] = 1
                ret += value
                counter_items += 1
        return -ret
