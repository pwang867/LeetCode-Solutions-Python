# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# divide and conquer
# one of root.left and root.right must be completely filled
# time O(h^2)


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = root, root
        height = 0
        while right:                   # right edge must reach the end no later than left edge
            right = right.right
            left = left.left
            height += 1
        if not left:                   # the tree is completely filled
            return 2**height - 1
        else:
            return self.countNodes(root.left) + 1 + self.countNodes(root.right)
        
        
"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
