# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create brand new ListNode, space/time O(m + n)
        dummy = ListNode(0)
        head = dummy
        carry = 0  # don't forget
        
        while l1 or l2 or carry:
            cur = carry
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            
            carry = cur//10
            cur = cur%10
            node = ListNode(cur)
            
            head.next = node
            head = head.next
            
        return dummy.next

        
