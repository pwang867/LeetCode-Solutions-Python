# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        self.res = -float('inf')
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        # return (min_val, max_val) in the subtree rooted at root
        if not root:
            return (float('inf'), -float('inf'))
        if not root.left and not root.right:
            return (root.val, root.val)
        min_left, max_left = self.dfs(root.left)
        min_right, max_right = self.dfs(root.right)
        self.res = max(self.res, abs(root.val - min(min_left, min_right)))
        self.res = max(self.res, abs(root.val - max(max_left, max_right)))
        return (min([min_left, min_right, root.val]), max([max_left, max_right, root.val]))


"""
Given the root of a binary tree, find the maximum value V for which there exists different 
nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
