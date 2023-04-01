# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class Trie:
    """
    Just to sets. one for prefixes and one for words.
    """

    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        prefix = ""
        for l in word:
            prefix += l
            self.prefixes.add(prefix)
        self.words.add(prefix)

    def search(self, word: str) -> bool:
        return True if word in self.words else False

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.prefixes else False
