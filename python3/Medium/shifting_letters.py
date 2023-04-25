from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        new_shifts =  [0]*len(shifts)
        carry,curr = 0,len(shifts)-1
        ret = ""
        letters = "abcdefgijknmlopqrstuvwxyz"
        letter_to_index = {}
        index_to_letter = {}
        for i in range(len(shifts)-1,-1,-1):
            carry += shifts[i]
            new_shifts[curr] = carry
            curr -= 1
        print(new_shifts)
        for i in range(len(letters)):
            letter_to_index[letters[i]] = i + 1
            index_to_letter[i+1] = letters[i]
        for index in range (len(s)):
            new_letter_index = (letter_to_index[s[index]]+new_shifts[index]) % len(letters)
            ret += index_to_letter[new_letter_index]
        return ret

s = "abc"
shifts = [3,5,9] #"rpl"
n = Solution()
print(n.shiftingLetters(s,shifts))


# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.