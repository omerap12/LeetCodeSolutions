# https://leetcode.com/problems/linked-list-random-node/
import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Two option:
    1. Save the nodes value and then getRandom will be in O(1)
    2. Just save the list length and random will generate a number -> get node value with that index
    """
    def __init__(self, head: Optional[ListNode]):
        self.nodes_value = []
        while head:
            self.nodes_value.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes_value)