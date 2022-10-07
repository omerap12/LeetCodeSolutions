# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        counterA,counterB = 0,0
        pointerA = headA
        while pointerA.next is not None:
            counterA+=1
            pointerA = pointerA.next
        pointerB = headB
        while pointerB.next is not None:
            counterB += 1
            pointerB = pointerB.next

        if counterB > counterA:
            difference = counterB-counterA
            for i in range(difference):
                headB = headB.next

        if counterA > counterB:
            difference = counterA - counterB
            for i in range(difference):
                headA= headA.next
        return self.check_intersect_even_lists(headA,headB)

    def check_intersect_even_lists(self,headA,headB):
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
