# time O(n), space O(1)
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy  # we swap the pair after p1
        
        while p1 and p1.next and p1.next.next:
            p2 = p1.next
            p3 = p2.next
            p4 = p3.next
            # swap middle two pointers: p2 and p3
            p1.next = p3
            p3.next = p2
            p2.next = p4
            
            p1 = p2
        
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
