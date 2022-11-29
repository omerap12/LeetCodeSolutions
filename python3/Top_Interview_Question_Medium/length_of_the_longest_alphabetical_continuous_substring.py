# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
class Solution(object):
    """
    sliding window algorithm
    """
    def longestContinuousSubstring(self, s):
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters_length = len(letters)
        dict_letter = {}
        for i in range(letters_length):
            dict_letter[letters[i]] = i
        length_s = len(s)
        sliding_window = []
        counter = 0
        max_counter = 0
        for i in range(length_s):
            if i == 0:
                sliding_window.append(s[i])
                counter = 1
                max_counter = 1
            else:
                if dict_letter[sliding_window[-1]]+1 == dict_letter[s[i]]:
                    counter += 1
                else:
                    sliding_window.clear()
                    counter = 1
                sliding_window.append(s[i])
                max_counter = max(max_counter, counter)
        return max_counter
