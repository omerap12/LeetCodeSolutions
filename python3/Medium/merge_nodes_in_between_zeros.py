# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    TO pointers, on to accumulate values and one to assimilate values
    """
    def mergeNodes(self, head):
        ass_pointer = head
        acc_pointer = head.next
        value_sum = 0
        while acc_pointer:
            if acc_pointer.val == 0:
                ass_pointer.val = value_sum
                acc_pointer = acc_pointer.next
                if not acc_pointer:
                    ass_pointer.next = None
                ass_pointer = ass_pointer.next
                value_sum = 0
            else:
                value_sum += acc_pointer.val
                acc_pointer = acc_pointer.next
        return head

head = ListNode(0,ListNode(3,ListNode(1,ListNode(0,ListNode(4,ListNode(5,ListNode(2,ListNode(0))))))))
n = Solution()
l = n.mergeNodes(head)
while l:
    print(l.val)
    l = l.next
