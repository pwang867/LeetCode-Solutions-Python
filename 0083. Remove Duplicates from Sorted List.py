# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        pre = head
        cur = head.next
        while cur:
            if pre.val != cur.val:
                pre = pre.next
                cur = cur.next
            else:
                cur = cur.next
                pre.next = cur
        
        return head


"""
Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
