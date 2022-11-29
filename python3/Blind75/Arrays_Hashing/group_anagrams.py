# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        dict_letters = {}
        counter = 0
        answer = []
        for i in range(len(strs)):
            sorted_word = tuple(sorted(strs[i]))
            if sorted_word in dict_letters.keys():
                answer[dict_letters[sorted_word]].append(strs[i])
            else:
                answer.append([strs[i]])
                dict_letters[sorted_word] = counter
                counter += 1
        return answer
