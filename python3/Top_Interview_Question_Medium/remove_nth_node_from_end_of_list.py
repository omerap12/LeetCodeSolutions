# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        nodes_length = 0
        tmp_head = head
        head_remove_pointer = head
        while tmp_head is not None:
            nodes_length += 1
            tmp_head = tmp_head.next
        node_to_remove = nodes_length-n
        if node_to_remove == 0:
            return head.next
        for i in range(node_to_remove-1):
            head_remove_pointer = head_remove_pointer.next
        head_remove_pointer.next = head_remove_pointer.next.next
        return head


n = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
head = n.removeNthFromEnd(head,2)
while head is not None:
    print(head.val)
    head = head.next
