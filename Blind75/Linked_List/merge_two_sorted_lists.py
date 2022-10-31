# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        tmp_head = head
        while list1 is not None or list2 is not None:
            if not list1:
                while list2:
                    tmp_head.next = ListNode(list2.val)
                    tmp_head = tmp_head.next
                    list2 = list2.next
            elif not list2:
                while list1:
                    tmp_head.next = ListNode(list1.val)
                    tmp_head = tmp_head.next
                    list1 = list1.next
            else:
                if list1.val < list2.val:
                    tmp_head.next = ListNode(list1.val)
                    tmp_head = tmp_head.next
                    list1 = list1.next
                else:
                    tmp_head.next = ListNode(list2.val)
                    tmp_head = tmp_head.next
                    list2 = list2.next
        return head.next

list1 = ListNode(-9,ListNode(3))
list2 = ListNode(5,ListNode(7))
n = Solution()
combine = n.mergeTwoLists(list1,list2)
while combine is not None:
    print(combine.val)
    combine = combine.next
