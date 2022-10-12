class Solution(object):
    def longestPalindrome(self, s):
        """
        for each index we check if it's the middle index of a bigger palindrome, were doing it by getting from the middle index outside with two pointers
        """
        stop_index = len(s)
        palindrome = ""
        palindrome_length = 0
        for i in range(stop_index):
            # odd cases
            left_pointer = i
            right_pointer = i
            # checking that pointers are in bounds and we have palindrome
            while right_pointer < stop_index and left_pointer >= 0 and s[left_pointer] == s[right_pointer]:
                # checking if length is max
                if right_pointer - left_pointer + 1 > palindrome_length:
                    palindrome_length = right_pointer - left_pointer + 1
                    palindrome = s[left_pointer:right_pointer + 1]
                # keep moving outside
                left_pointer -= 1
                right_pointer += 1

            # even cases
            left_pointer = i
            right_pointer = i + 1
            while right_pointer < stop_index and left_pointer >= 0 and s[left_pointer] == s[right_pointer]:
                # checking if length is max
                if right_pointer - left_pointer + 1 > palindrome_length:
                    palindrome_length = right_pointer - left_pointer + 1
                    palindrome = s[left_pointer:right_pointer + 1]
                # keep moving outside
                left_pointer -= 1
                right_pointer += 1

        return palindrome

