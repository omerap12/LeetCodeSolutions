#Solution to: https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        answer = {} # key - sorted word, value - original word 
        for i in range(len(strs)):
            sorted_name ="".join(sorted(strs[i]))
            # if word is already in the bank
            if sorted_name in answer.keys():
                answer[sorted_name].append(strs[i])
            else:
              # create new bank for the word
                answer[sorted_name] = [strs[i]]
        return [word for word in answer.values()]
