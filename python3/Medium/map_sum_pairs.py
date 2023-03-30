# https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:
    """
    The key is to create two maps: one for word -> val. another for prefix -> val.
    When insert a word check if the word already in the inventory, if so calculate the value diff. and for each
    prefix of the word add that diff.
    if the word is not in the inventory, add her and for each prefix add the word's value.
    """

    def __init__(self):
        self.word_inventory = {}  # word to val
        self.prefix_value = {}  # prefix to val

    def insert(self, key: str, val: int) -> None:
        if key not in self.word_inventory.keys():
            self.word_inventory[key] = val
            prefix = ""
            for l in key:
                prefix += l
                try:
                    self.prefix_value[prefix] += val
                except KeyError as e:
                    self.prefix_value[prefix] = val
        else:
            diff = val - self.word_inventory[key]
            self.word_inventory[key] = val
            prefix = ""
            for l in key:
                prefix += l
                self.prefix_value[prefix] += diff

    def sum(self, prefix: str) -> int:
        if prefix in self.prefix_value.keys():
            return self.prefix_value[prefix]
        else:
            return 0