# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0
        vowles = ('a', 'e', 'i', 'o','u')
        sliding_window = []
        ret = 0
        vowles_till_now = 0
        for l in s:
            if len(sliding_window) < k:
                if l in vowles:
                    vowles_till_now += 1
                sliding_window.append(l)
                ret = max(vowles_till_now,ret)
            else:
                if l in vowles:
                    vowles_till_now += 1
                popped_letter = sliding_window.pop(0)
                if popped_letter in vowles:
                    vowles_till_now -= 1
                sliding_window.append(l)
                ret = max(vowles_till_now,ret)
        ret = max(vowles_till_now,ret)
        return ret