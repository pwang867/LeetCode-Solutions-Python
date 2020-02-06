# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        maxSum = [root.val]
        self.maxSinglePathSum(root, maxSum)
        return maxSum[0]
    
    
    def maxSinglePathSum(self, root, maxSum):
        # the max sum of a path starting from and including the root
        if not root:
            return 0
        
        leftmax = self.maxSinglePathSum(root.left, maxSum)
        rightmax = self.maxSinglePathSum(root.right, maxSum)
        
        maxSum[0] = max(maxSum[0], max(0, leftmax) + max(0, rightmax) + root.val)
        
        return root.val + max([0, leftmax, rightmax])


"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from 
some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
