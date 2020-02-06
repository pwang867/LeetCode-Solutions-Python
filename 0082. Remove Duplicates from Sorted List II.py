# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur:
            if not cur.next or cur.val != cur.next.val:
                pre.next = cur
                pre = pre.next
                cur = cur.next
            else:
                duplicate = cur.val
                while cur and cur.val == duplicate:
                    cur = cur.next
                pre.next = cur
                # don't move pre and cur at this point!
                # cur is not validated yet
        
        return dummy.next
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# head may be deleted
# note: delete all duplicates, don't keep one
class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate = cur.val
                while cur and cur.val == duplicate:
                    cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        
        pre.next = None  # don't forget
        
        return dummy.next
        


"""
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

