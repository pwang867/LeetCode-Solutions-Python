# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 2
# without using extra space, time O(n), space O(1)
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        slow = head.next  # mistake: slow = head, fast = head.next
        fast = head.next.next
        
        # stop when a cycle if found or when reading the end
        while slow != fast and fast and fast.next:   # don't forget fast and fast.next
            slow = slow.next
            fast = fast.next.next
        
        if not fast or not fast.next:  # when no cycle
            return None
        
        pos = head
        while pos != slow:
            pos = pos.next
            slow = slow.next
        
        return pos

# method 1, hashset, using extra space, time O(n), space O(n)
class Solution(object):
    def detectCycle(self, head):
        
        visited = set()
        p = head
        while p:
            if p in visited:
                return p
            visited.add(p)
            p = p.next
        
        return p
    
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""
