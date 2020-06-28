# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time O(n), extra recursion space O(depth) except the result itself


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        self.index = 0
        return self.dfs(preorder, -float('inf'), float('inf'))

    def dfs(self, preorder, low, high):
        if self.index == len(preorder):
            return None
        val = preorder[self.index]
        if not (low <= val <= high):
            return None
        root = TreeNode(val)
        self.index += 1
        root.left = self.dfs(preorder, low, val)
        root.right = self.dfs(preorder, val, high)
        return root


"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left 
has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder 
traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""