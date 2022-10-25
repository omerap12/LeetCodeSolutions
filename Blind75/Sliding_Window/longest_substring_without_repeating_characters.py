# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sliding_window_cache = set()
        sliding_window = []
        max_size = 0
        for word in s:
            if word not in sliding_window_cache:
                sliding_window_cache.add(word)
                sliding_window.append(word)
            else:
                while sliding_window[0] != word:
                    sliding_window.pop(0)
                sliding_window.pop(0)
                sliding_window.append(word)
                sliding_window_cache = set(sliding_window)
            max_size = max(max_size, len(sliding_window))
        return max_size
