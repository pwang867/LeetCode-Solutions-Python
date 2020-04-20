# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

# method 3, similar to method 2, but use a wrapper instead of using (val, node) pairs


class MyNode:
    def __init__(self, list_node):
        self.list_node = list_node

    def __lt__(self, node):
        if not self.list_node:
            return False
        if not node.list_node:
            return True
        return self.list_node.val < node.list_node.val


class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [MyNode(node) for node in lists if node]
        heapq.heapify(h)
        dummy = ListNode(0)
        cur = dummy
        while h:
            node = heapq.heappop(h)
            cur.next = node.list_node
            cur = cur.next
            if node.list_node.next:
                heapq.heappush(h, MyNode(node.list_node.next))
        return dummy.next


# method 2, heap, time O(n*k*log(k)), space O(n*k)
class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(node.val, node) for node in lists if node]
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        return dummy.next


# method 1, divide and conquer
# time: O(n*k*logk), space O(n*k)
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        # merge
        n = len(lists)
        while n > 1:
            mid = (n + 1)//2  # divide by mid, mid is also the distance between two halves
            for i in range(n//2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + mid])    
            n = mid
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        curr = head
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1:  # mistake: if not l1
            curr.next = l1
        else:
            curr.next = l2
            
        return head.next



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    
"""
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


