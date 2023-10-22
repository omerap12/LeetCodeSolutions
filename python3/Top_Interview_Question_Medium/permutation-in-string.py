# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    # Sliding window + anagrams
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict,count_letters = {},{}        
        for l in s1:
            s1_dict[l] = 1 + s1_dict.get(l,0)
        sliding_window = []
        for word in s2:
            if len(sliding_window) < len(s1):
                sliding_window.append(word)
                count_letters[word] = 1 + count_letters.get(word,0)
            else:
                if s1_dict.items() == count_letters.items():
                    return True
                popped_word = sliding_window.pop(0)
                count_letters[popped_word] = count_letters[popped_word] - 1
                if count_letters[popped_word] == 0:
                    del count_letters[popped_word]
                sliding_window.append(word)
                count_letters[word] = 1 + count_letters.get(word,0)
        return True if s1_dict.items() == count_letters.items() else False
