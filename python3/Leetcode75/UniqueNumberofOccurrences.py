# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        number_of_occ = {}
        for number in arr:
            if number in number_of_occ.keys():
                number_of_occ[number] += 1
            else:
                number_of_occ[number] = 1
        
        values = [v for v in number_of_occ.values()]
        if len(values) == len(set(values)):
            return True
        return False