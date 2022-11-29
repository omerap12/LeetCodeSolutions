#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        queue is the sliding window, we add new letters to the window (and update max accordingly) and remove items from left side of the window until we removed the letter that has already been shown. set is for the 0(1) time finding the letter.
        """
        queue = []
        window = set()
        length_max = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.add(s[i])
                queue.append(s[i])
                if length_max < len(queue):
                    length_max = len(queue)
            else:
                word = ""
                while word != s[i]:
                    word = queue.pop(0)
                    window.remove(word)
                queue.append(s[i])
                window.add(s[i])
        return length_max
