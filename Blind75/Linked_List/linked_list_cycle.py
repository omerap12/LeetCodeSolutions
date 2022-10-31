# https://leetcode.com/problems/linked-list-cycle/

class Solution(object):
    def hasCycle(self, head):
        turtle = head
        rabbit = head
        first_used = True
        while turtle is not None and rabbit is not None:
            if turtle.next is None or rabbit.next is None or rabbit.next.next is None:
                return False
            if not first_used:
                if turtle == rabbit:
                    return True
            turtle = turtle.next
            rabbit = rabbit.next.next
            first_used = False
        return False
