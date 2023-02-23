# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        appearnces = {}
        for char in s:
            if char in appearnces.keys():
                appearnces[char] += 1
            else:
                appearnces[char] = 1
        bag = [(v, k) for k, v in appearnces.items()]
        bag.sort(reverse=True)
        return "".join(l[1]*l[0] for l in bag)