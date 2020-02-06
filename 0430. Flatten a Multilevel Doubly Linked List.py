"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# time/space O(n)
# this method uses recursion
# another method: we can actually regard this linkedlist as 
# a tree, and use stack with pre-order traversal
# ref: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/154908/Python-easy-solution-using-stack
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        dummy = Node(0, None, None, None)
        self.flattenHelper(dummy, head)
        dummy.next.prev = None
        return dummy.next
    
    def flattenHelper(self, pre, cur):
        while cur:
            pre.next = cur
            cur.prev = pre
            pre = pre.next
            if cur.child:
                new_head = cur.child
                copy = cur.next
                cur.child = None
                tail = self.flattenHelper(cur, new_head)
                pre = tail
                cur = copy
            else:
                cur = cur.next
        return pre
    

"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""
