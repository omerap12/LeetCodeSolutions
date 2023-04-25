# https://leetcode.com/problems/shifting-letters/description/

from typing import List
import string 

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        The solution is in two parts:
        1. We calculate a new_shifts array where the array[i] is how much shifts does the s[i] gets.
            we calulate this by iterating shifts array backwords and set new_shifts[i] = how much we have accumalted till the ith index (backwords)
        2. After we calaculate the new_shifts array we create an index -> letter and letter -> index map and.
            To caculate the new letter we first gets it index, then add the new_shifts and if neccessay using modulo, then convert the index back to letter.
        """
        new_shifts =  [0]*len(shifts)
        carry,curr = 0,len(shifts)-1
        ret = ""
        letters = string.ascii_lowercase
        letter_to_index = {}
        index_to_letter = {}
        for i in range(len(shifts)-1,-1,-1):
            carry += shifts[i]
            new_shifts[curr] = carry
            curr -= 1
        for i in range(len(letters)):
            letter_to_index[letters[i]] = i
            index_to_letter[i+1] = letters[i]
        for index in range (len(s)):
            new_letter_index = (letter_to_index[s[index]]+new_shifts[index]) % len(letters) + 1
            ret += index_to_letter[new_letter_index]
        return ret