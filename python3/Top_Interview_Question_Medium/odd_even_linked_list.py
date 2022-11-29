# https://leetcode.com/problems/odd-even-linked-list/


class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd_head = head
        copy_odd_head = odd_head
        even_head = head.next
        copy_even_head = head.next
        while odd_head and even_head:
            if even_head.next is None:
                break
            odd_head.next = even_head.next
            odd_head = odd_head.next
            if odd_head:
                even_head.next = odd_head.next
                even_head = even_head.next
        odd_head.next = copy_even_head
        return copy_odd_head
