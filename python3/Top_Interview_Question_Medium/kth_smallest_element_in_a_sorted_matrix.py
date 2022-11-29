# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []
        for row in matrix:
            heap += row
        heapq.heapify(heap)
        counter = 0
        while heap and counter < k:
            counter += 1
            number = heapq.heappop(heap)
        return number
