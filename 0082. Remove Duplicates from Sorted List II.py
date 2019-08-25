# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur:
            if not cur.next or cur.val != cur.next.val:
                pre.next = cur
                pre = pre.next
                cur = cur.next
            else:
                duplicate = cur.val
                while cur and cur.val == duplicate:
                    cur = cur.next
                pre.next = cur
                # don't move pre and cur at this point!
                # cur is not validated yet
        
        return dummy.next
        
        
