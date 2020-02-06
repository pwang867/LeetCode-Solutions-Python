# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# time O(n), space O(k)
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [None for _ in range(k)]
        
        # find the length of root
        length = 1
        cur = root
        while cur.next:
            cur = cur.next
            length += 1
        
        cnt, extra = divmod(length, k)
        
        ans = []
        pre = ListNode(0)
        cur = root
        for i in range(k):
            # find the size of i-th block
            if extra > 0:
                size = cnt + 1
                extra -= 1
            else:
                size = cnt
            # save ListNode into block
            ans.append(cur)
            for _ in range(size):
                pre = cur
                cur = cur.next
            pre.next = None
        
        return ans


"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
"""
