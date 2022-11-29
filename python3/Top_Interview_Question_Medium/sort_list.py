# https://leetcode.com/problems/sort-list/
class Solution(object):
    def sortList(self, head):
        values = []
        tmp = head
        while tmp is not None:
            values.append(tmp.val)
            tmp = tmp.next
        values.sort()
        if values:
            new_head = ListNode(values[0])
            new_tmp = new_head
        else:
            return None
        for i in range(1,len(values),1):
            new_tmp.next = ListNode(values[i])
            new_tmp = new_tmp.next
        return new_head
