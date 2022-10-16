# https://leetcode.com/problems/top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        counter_number = {}
        for number in nums:
            if number in counter_number.keys():
                counter_number[number] = counter_number[number] + 1
            else:
                counter_number[number] = 1
        res = sorted(counter_number.items(), key=lambda x: x[1],reverse=True)
        answer = []
        for i in range(k):
            answer.append(res[i][0])
        return answer
