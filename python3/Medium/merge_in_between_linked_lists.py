# https://leetcode.com/problems/merge-in-between-linked-lists/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        Get two pointers at the two edges of the linked list (edge a and edge b).
        To remove the a'th node and the b'th node set the edges to be (a-1,b+1).
        Then set edge a pointer.next = list2 and list2_last_node.next = b pointer.
        """
        index_fptr = 0
        fptr = list1
        index_sptr = 0
        sptr = list1
        list2_ptr = list2

        while index_fptr != a-1:
            fptr = fptr.next
            index_fptr += 1
        while index_sptr != b+1:
            sptr = sptr.next
            index_sptr += 1

        fptr.next = list2_ptr
        while list2_ptr.next is not None:
            list2_ptr = list2_ptr.next

        list2_ptr.next = sptr
        return list1