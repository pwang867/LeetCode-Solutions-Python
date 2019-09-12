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
        
        slow = head.next  # mistake: slow = head
        fast = head.next.next
        
        # stop when a cycle if found or when reading the end
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if not fast or not fast.next:  # when no cycle
            return None
        
        pos = head
        while pos != slow:
            pos = pos.next
            slow = slow.next
        
        return pos

# method 1, using extra space, time O(n), space O(n)
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
    
