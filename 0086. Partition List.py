# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# use two linkedlist to help partition
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0)  # save val less than x
        tail1 = head1
        head2 = ListNode(0)  # <= x
        tail2 = head2
        
        while head:
            if head.val < x:
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
        
        tail1.next = head2.next
        tail2.next = None
        
        return head1.next
    
