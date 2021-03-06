# Two pointers, one pass, O(n)
# first pointer moved n-step ahead of second pointer
# move n-1 steps first, then move the n-th step separately


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        for _ in range(n + 1):
            if not fast:
                return dummy.next
            fast = fast.next
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        if slow and slow.next:
            slow.next = slow.next.next
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def create_linkedlist(nums):
    head = ListNode(0)
    cur = head
    for i, num in enumerate(nums):
        cur.next = ListNode(num)
        cur = cur.next
    return head.next

def print_linkedlist(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    head = create_linkedlist(nums)
    res = Solution().removeNthFromEnd(head, 2)
    print_linkedlist(res)

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""