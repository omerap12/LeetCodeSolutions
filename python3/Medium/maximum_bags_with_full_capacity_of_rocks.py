# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        Observation: We want to fill the bags that need the least rocks to be full. 
        """
        rocks_missing = [capacity[i] - rocks[i] for i in
                         range(len(capacity))]  # calculate for each bag how many stones needs
        rocks_missing.sort()
        for i in range(len(rocks_missing)):
            if additionalRocks - rocks_missing[i] >= 0:  # check if we have enough stones to fill the bag
                additionalRocks -= rocks_missing[i]
                rocks_missing[i] = 0
            else:
                break
        return rocks_missing.count(0)
