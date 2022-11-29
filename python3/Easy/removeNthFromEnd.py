#Solution to: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        copy_head = head
        length_of_list = self.get_length(head) # get the length of the linked list
        if length_of_list == n: # if the head is the one to remove
            head = head.next
            return head
        times = length_of_list - n - 1 # get pointer on Node before the desireable removal one
        for i in range(times):
            copy_head = copy_head.next
        copy_head.next = copy_head.next.next # remove Node
        return head

    def get_length(self, head): # get the length of the linked list
        counter = 1
        while head.next is not None:
            head = head.next
            counter += 1
        return counter
