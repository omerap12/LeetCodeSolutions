# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = 0
        for i in range(len(arr)//2):
            res = max(res,arr[i]+arr[len(arr)-1-i])
        return res


head = ListNode(5,ListNode(4,ListNode(2,ListNode(1))))
n = Solution()
print(n.pairSum(head))
