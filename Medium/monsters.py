#Solution To: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

import heapq
import math

class Solution(object):
  # get for each monster in how many turns it will reach the city, than put the data in min-heap.
    def eliminateMaximum(self, dist, speed):
        turns = self.getMonstersTurns(dist, speed)
        current_meter = 0
        heapq.heapify(turns)  # create the min heap
        while len(turns) != 0:
            current_monster = heapq.heappop(turns)  # get the min value
            if current_monster == current_meter:
                return current_meter
            current_meter += 1
        return current_meter

    def getMonstersTurns(self, dist, speed):
        turns_until_here = []
        for i in range(len(dist)):
            turns_until_here.append(math.ceil(dist[i] / speed[i]))
        return turns_until_here
