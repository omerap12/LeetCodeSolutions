Solution to: https://leetcode.com/problems/add-two-numbers/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        combine = list(
            str(self.getNumber(l1) + self.getNumber(l2))[::-1])  # get the sum of the list, [::-1] for backward 
        if len(combine) == 0:
            return ListNode()
        head = ListNode(combine[0])
        head2 = head
        for i in range(1, len(combine), 1):
            head.next = ListNode(int(combine[i]))  # add the values to next
            head = head.next
        return head2

    def getNumber(self, l):  # get the value of the list
        string_number = ""
        while l:
            string_number += str(l.val)
            l = l.next
        return int(string_number[::-1])  # return the number backward
