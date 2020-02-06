# time O(n), space O(1)

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        
        while p1:
            next_p1 = p1.next
            cur = p1.next  # pre and cur are used for reversing
            pre = p1.next
            # get a k-len-group
            for _ in range(k):
                if pre:
                    pre = pre.next
                else:  # when the last group size is < k
                    return dummy.next
            # reverse the k-group
            for _ in range(k):  # for loop is important to control the termination
                copy = cur.next
                cur.next = pre
                pre = cur
                cur = copy
            # connect k-groups
            p1.next = pre
            # reset all pointers
            p1 = next_p1
        
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Given a linked list, reverse the nodes of a linked list k at a time and 
return its modified list.

k is a positive integer and is less than or equal to 
the length of the linked list. 
If the number of nodes is not a multiple of k then 
left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

