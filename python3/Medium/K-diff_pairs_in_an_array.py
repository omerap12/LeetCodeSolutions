# https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/

class Solution:
    def findPairs(self, nums, k):
        dict_numbers = {}
        set_answer = set()
        for number in nums:
            if number in dict_numbers.keys():
                dict_numbers[number] += 1
            else:
                dict_numbers[number] = 1
        for number in nums:
            if k == 0:
                if dict_numbers[number] > 1:
                    set_answer.add(tuple((number, number)))
            else:
                if number + k in dict_numbers.keys():
                    set_answer.add(tuple((number, number + k)))
        return len(set_answer)

