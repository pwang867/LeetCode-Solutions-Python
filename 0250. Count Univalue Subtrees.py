# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.isSameValue(root)
        return self.res
    
    def isSameValue(self, root):
        # return (tree is same value, the value)
        if not root:
            return (True, None)
        left_is_same, left_val = self.isSameValue(root.left)
        right_is_same, right_val = self.isSameValue(root.right)
        if left_is_same and right_is_same and \
        (left_val is None or left_val == root.val) \
        and (right_val is None or right_val == root.val):
            self.res += 1
            return (True, root.val)
        return (False, None)


"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""
    