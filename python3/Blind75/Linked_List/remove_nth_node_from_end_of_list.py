# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Do the removement with one pass, save the nodes in dict and get the 
        node to be deleted by calculating it's index
        """
        nodes_dict = {}
        tmp_head = head
        counter = 0
        while tmp_head:
            nodes_dict[counter] = tmp_head
            tmp_head = tmp_head.next
            counter += 1
        # if remove the head
        if n == counter:
            return head.next
        index_to_remove = counter - n
        # if remove the last
        if n == 1:
            nodes_dict[index_to_remove-1].next = None
        else:
            # else
            nodes_dict[index_to_remove-1].next = nodes_dict[index_to_remove+1]
        return head

n = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
new_head = n.removeNthFromEnd(head,1)
while new_head:
    print(new_head.val)
    new_head = new_head.next
