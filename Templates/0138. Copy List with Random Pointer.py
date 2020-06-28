class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# clone nodes first, then clone the connections between them
# note: many random pointers may point to None, not only the last node

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # copy every node, don't set the randome pointer yet
        # the copied node is inserted right after the original node
        p1 = head
        while p1:
            p2 = p1.next
            new_node = Node(p1.val, p2, None)
            p1.next = new_node
            p1 = p2
        
        # set the random pointer
        p1 = head
        while p1:
            if p1.random:  # p1.random might be None !!!
                p1.next.random = p1.random.next
            p1 = p1.next.next
        
        # separate original list and the newly copied list
        dummy = Node(0, None, None)
        cur = dummy
        p1 = head
        while p1:
            p2 = p1.next
            p3 = p2.next
            cur.next = p2
            cur = cur.next
            p1.next = p3
            p1 = p3
        if cur:
            cur.next = None
        
        return dummy.next



"""
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""
