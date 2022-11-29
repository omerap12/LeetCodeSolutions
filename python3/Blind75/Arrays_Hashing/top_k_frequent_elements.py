# https://leetcode.com/problems/top-k-frequent-elements/

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        dict_counter = {}
        for number in nums:
            if number not in dict_counter:
                dict_counter[number] = 1
            else:
                dict_counter[number] += 1
        # stores (-appearance_number ,number) in min heap
        tuples_heap = []
        for key, value in dict_counter.items():
            tuples_heap.append((-value, key))
        heapq.heapify(tuples_heap)
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(tuples_heap)[1])
        return answer
