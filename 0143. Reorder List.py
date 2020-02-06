# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # slice the linked list into half
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None  # cut the list into half, right half will be no longer than left half
        
        # reverse the second half, head2
        head2 = self.reverse(head2)
        
        # combine the two halves in a new way
        p1, p2 = head, head2
        while p1 and p2:
            copy1 = p1.next
            copy2 = p2.next
            p1.next = p2
            p2.next = copy1
            p1, p2 = copy1, copy2
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            copy = cur.next
            cur.next = pre
            pre, cur = cur, copy
        return pre

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
