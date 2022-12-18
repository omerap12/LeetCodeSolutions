# https://leetcode.com/problems/remove-nodes-from-linked-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    We need to know for each node its right maximum value -> reverse travers using stack and saving the max value.
    """
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        tmp_head = head.next
        prev_head = head
        while tmp_head:
            stack.append((prev_head, tmp_head))
            prev_head = prev_head.next
            tmp_head = tmp_head.next
        max_val = float('-inf')
        while stack:
            prev, cur = stack.pop()
            max_val = max(max_val, cur.val)
            if cur.val < max_val:
                prev.next = cur.next
        if head.val < max_val:
            head = head.next
        return head