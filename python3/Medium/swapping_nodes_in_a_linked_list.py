# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        One loop to count the nodes, another loop to find the first and last node and switch them.
        """
        res = head
        first_node = head
        last_node = head
        counter_ptr = head
        counter_node = 0
        while counter_ptr:
            counter_node += 1
            counter_ptr = counter_ptr.next

        first_node_found = False
        last_node_found = False
        for step in range(counter_node):
            if step == k-1:
                first_node_found = True
            if step == counter_node - k:
                last_node_found = True
            if last_node_found and first_node_found:
                break
            if not last_node_found:
                last_node = last_node.next
            if not first_node_found:
                first_node = first_node.next
        if first_node != last_node:
            tmp = first_node.val
            first_node.val = last_node.val
            last_node.val = tmp
        return res