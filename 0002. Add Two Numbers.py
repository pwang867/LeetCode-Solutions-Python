from linkedlist import ListNode, list_to_linkedlist

# create a brand new ListNode for the answer, space/time O(m + n)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0   # don't forget initialization
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
    
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

if __name__ == "__main__":
    nums1 = [2, 4, 3, 9]
    nums2= [5, 6, 7]
    l1 = list_to_linkedlist(nums1)
    l2 = list_to_linkedlist(nums2)
    
    Solution().addTwoNumbers(l1, l2).print_node()
    