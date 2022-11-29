class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first_word = strs[0]
            common_prefix = ""
            for i in range(len(first_word)):
                l = first_word[i]
                if self.check_letter(l, i, strs):
                    common_prefix = common_prefix + l
                else:
                    return common_prefix
            return common_prefix

    def check_letter(self, letter, index, strs):
        for word in strs:
            if len(word)-1 < index:
                return False
            if word[index] != letter:
                return False
        return True