# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1, iteration
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head 
        
        while cur:
            copy = cur.next
            cur.next = pre
            pre, cur = cur, copy
        
        return pre


# method 2, recursion
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head, tail = self.reverseHelper(head)
        tail.next = None
        return head
    
    def reverseHelper(self, head):
        # return the head and tail of the reversed list
        if not head.next:
            return head, head
        cur = head
        new_head, tail = self.reverseHelper(head.next)
        tail.next = cur
        return new_head, cur
    

    
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
