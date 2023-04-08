# https://leetcode.com/problems/implement-magic-dictionary/description/
from typing import List


class MagicDictionary:
    """
    The idea is to save for every word from the buildDict list, all the astrix in a dict.
    For example the word hello will be inserted:
    *ello -> [hello]
    h*llo -> [hello]
    .
    .
    .
    In the search method, we're again iterating through the astrix available locations, if found a version which
    has more than on word matching to it or the word that matching with it isn't the input word -> return True
    else, return False
    """

    def __init__(self):
        self.astrix_to_original = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for index in range(len(word)):
                if index == 0:
                    astrix_word = "*" + word[1:]
                else:
                    astrix_word = word[:index] + "*" + word[index + 1:]
                if astrix_word in self.astrix_to_original.keys():
                    self.astrix_to_original[astrix_word].append(word)
                else:
                    self.astrix_to_original[astrix_word] = [word]

    def search(self, searchWord: str) -> bool:
        for index in range(len(searchWord)):
            if index == 0:
                astrix_word_search = "*" + searchWord[1:]
            else:
                astrix_word_search = searchWord[:index] + "*" + searchWord[index + 1:]
            if astrix_word_search in self.astrix_to_original.keys() and \
                    (len(self.astrix_to_original[astrix_word_search]) > 1 or
                     searchWord not in self.astrix_to_original[astrix_word_search]):
                return True
        return False