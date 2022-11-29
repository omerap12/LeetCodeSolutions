# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next = None):
        self.val = x
        self.next = next

class Solution(object):
    def deleteNode(self, node):
        while True:
            if node.next.next is None:
                node.val = node.next.val
                node.next = None
                return
            node.val = node.next.val
            node = node.next



head = ListNode(4,ListNode(5,ListNode(1,ListNode(9,ListNode(10)))))
while head is not None:
    print(head.val,end="-> ")
    head = head.next
print("None")
n = Solution()
head = ListNode(4,ListNode(5,ListNode(1,ListNode(9,ListNode(10)))))
n.deleteNode(head.next)
while head is not None:
    print(head.val,end="-> ")
    head = head.next
print("None")

