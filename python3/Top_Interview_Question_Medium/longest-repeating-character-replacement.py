# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_letters, ret = {},0
        lptr = 0
        for rptr in range(len(s)):
            count_letters[s[rptr]] = 1 + count_letters.get(s[rptr],0)

            while (rptr - lptr + 1) - max(count_letters.values()) > k:
                count_letters[s[lptr]] -= 1
                lptr += 1

            ret = max(ret,rptr - lptr + 1)
        return ret
