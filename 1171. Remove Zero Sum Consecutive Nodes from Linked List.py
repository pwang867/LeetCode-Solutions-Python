# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# use OrderedDict, O(n)
from collections import OrderedDict
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        d = OrderedDict()
        d[0] = dummy
        cur = 0
        while head:
            cur += head.val
            if cur not in d:
                d[cur] = head
            else:
                last = d[cur]    # backup
                while cur in d:
                    d.popitem()
                d[cur] = last   # re-connect
                last.next = head.next
            head = head.next
        return dummy.next


# O(n)
class Solution1(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = 0
        d = {0: dummy}  # {sum of nums[:i]: node}
        while head:
            cur += head.val
            if cur in d:
                d[cur].next = head.next
                return self.removeZeroSumSublists(dummy.next)
            else:
                d[cur] = head
                head = head.next
                
        return dummy.next


"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""
