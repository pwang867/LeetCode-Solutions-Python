# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time O(n), space O(n) recursion depth
# this kind of height balance is a requirement for AVL tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHelper(root)[1]
    
    def isBalancedHelper(self, root):
        if not root:
            return (0, True)
        
        left_depth, left_is_balanced = self.isBalancedHelper(root.left)
        if not left_is_balanced:
            return (0, False)
        right_depth, right_is_balanced = self.isBalancedHelper(root.right)
        if not right_is_balanced or abs(left_depth - right_depth) > 1:
            return (0, False)
        
        return (1 + max(left_depth, right_depth), True)


"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
"""
