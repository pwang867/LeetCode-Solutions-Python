# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# pre is the last node that node.val != 9
# one pass, time O(n), space O(1)
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy
        while cur:
            if cur.val != 9:
                pre = cur
            cur = cur.next
        pre.val += 1   # pre is the last node that node.val != 9
        pre = pre.next
        while pre:
            pre.val = 0
            pre = pre.next
        return dummy if dummy.val == 1 else dummy.next
    


"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""
