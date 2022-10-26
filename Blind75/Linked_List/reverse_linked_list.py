# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return head
        stack = []
        tmp_head_head = head
        while tmp_head_head:
            stack.append(tmp_head_head.val)
            tmp_head_head = tmp_head_head.next
        new_list_head = ListNode(stack.pop())
        tmp_new_list_head = new_list_head
        while stack:
            tmp_new_list_head.next = ListNode(stack.pop())
            tmp_new_list_head = tmp_new_list_head.next
        return new_list_head

