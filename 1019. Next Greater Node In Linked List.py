# method 1: maintain a decreasing stack

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []  # decreasing, (val, index)
        index = 0
        next_larger = []
        
        while head:
            if stack and head.val > stack[-1][0]:
                while stack and head.val > stack[-1][0]:
                    val, i = stack.pop()
                    next_larger[i] = head.val
            stack.append((head.val, index))
            next_larger.append(0)  # assume it is not found in the beginning
            head = head.next
            index += 1  # don't forget
        
        return next_larger
    
