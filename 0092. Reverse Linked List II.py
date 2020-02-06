# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # to solve m==1 issue
        dummy = ListNode(0)
        dummy.next = head
        
        # initialize
        tail = dummy
        for i in range(m-1):
            tail = tail.next
        pre = tail.next
        cur = pre.next
        pre.next = None  # not mandatory
        
        # reverse
        for i in range(n-m):
            copy = cur.next  # to make sure cur.next is always valid !
            cur.next = pre
            pre, cur = cur, copy
        
        # reconnect
        copy = tail.next
        tail.next = pre
        copy.next = cur
        
        return dummy.next

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
