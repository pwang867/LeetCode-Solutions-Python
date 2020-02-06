# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time O(n), space O(log(n)) recursion depth + O(n) tree itself
class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        self.node = head
        return self.sortedListToBSTHelper(0, length-1)
    
    def sortedListToBSTHelper(self, left, right):
        # self.node is the left-th node when entering this function
        # and self.node becomes the right+1-th node when exiting this function
        if left > right:  # left and right index are only used to control termination
            return None
        
        mid = left + (right-left)//2    
        # (right-left+1)//2 is also OK, but right tree will higher
        
        ltree = self.sortedListToBSTHelper(left, mid-1)
        root = TreeNode(self.node.val)
        root.left = ltree
        
        self.node = self.node.next
        rtree = self.sortedListToBSTHelper(mid+1, right)
        root.right = rtree
        
        return root


# time O(n*log(n)), space O(log(n)) recursion depth + O(n) tree itself
class Solution1(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:  # can not forget
            return TreeNode(head.val)
        
        slow, fast = head, head
        tail = head
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val)
        tail.next = None
        root.right = self.sortedListToBST(slow.next)
        root.left = self.sortedListToBST(head)
        
        return root


"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

