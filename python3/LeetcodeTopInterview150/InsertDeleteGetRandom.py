# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
import random

class RandomizedSet:

    def __init__(self):
        self.members = set()
        self.members_length = 0

    def insert(self, val: int) -> bool:
        if val not in self.members:
            self.members.add(val)
            self.members_length += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.members:
            self.members.remove(val)
            self.members_length -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.members))