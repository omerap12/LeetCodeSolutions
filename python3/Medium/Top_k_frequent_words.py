# https://leetcode.com/problems/top-k-frequent-words/
import heapq
class Solution:
    def topKFrequent(self, words, k):
        dict_words = {}
        for word in words:
            if word in dict_words.keys():
                dict_words[word] += 1
            else:
                dict_words[word] = 1
        min_heap = [(-count,word) for word,count in dict_words.items()]
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res