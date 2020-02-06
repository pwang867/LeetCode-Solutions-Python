# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time O(n), space O(1) in place
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        pre, cur = None, head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            copy = cur.next  
            cur.next = pre  # reverse the first half
            pre, cur = cur, copy
        
        if fast:  # original list has even length
            if cur.val != cur.next.val:
                return False
            return self.isSameList(pre, cur.next.next)
        else:  # odd length
            return self.isSameList(pre, cur.next)
    
    def isSameList(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return not head1 and not head2


"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
