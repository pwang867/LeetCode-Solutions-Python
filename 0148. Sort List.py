# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:25:27 2019

@author: WEIMIN ZHOU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n*log(n))


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        # divide in half --> sort two halves --> merge two halves
        head1, head2 = self.divide(head)
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)
        
    def divide(self, head):
        if not head:
            return None, None
        if not head.next:
            return head, None
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next  # head2 will not be longer than head
        slow.next = None  # cut in half
        return head, head2
        
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val > head2.val:
                cur.next = head2
                cur = cur.next
                head2 = head2.next
            else:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
        if head1:
            cur.next = head1
        else:
            cur.next = head2
        return dummy.next
    

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
