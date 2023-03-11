# https://leetcode.com/problems/two-city-scheduling/
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        The idea is to send every person to A and then send half of the people to B.
        But which people? the pople who would refund us with the maximum val
        """
        refund_arr = []
        res = 0
        for person in costs:
            refund_arr.append(person[0]-person[1])
            res += person[0]
        refund_arr.sort(reverse=True)
        # refund_arr at index i is the money received by transport person i to B instead of A

        for i in range(len(costs)//2):
            res -= refund_arr[i]
        return res
