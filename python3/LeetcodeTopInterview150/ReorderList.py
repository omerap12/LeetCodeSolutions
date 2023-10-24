# https://leetcode.com/problems/reorder-list/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       stack = []
       tmp_head = head.next
       while tmp_head:
           stack.append(tmp_head)
           tmp_head = tmp_head.next
       
       temp = head
       while stack:
           temp.next = stack.pop()
           temp = temp.next
           if stack:
            temp.next = stack.pop(0)
            temp = temp.next
       temp.next = None
       return head
