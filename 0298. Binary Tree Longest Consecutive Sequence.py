# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        self.longestConsecutiveHelper(root)
        return self.longest
    
    def longestConsecutiveHelper(self, root):
        # find the longest consecutive path starting from root to any node
        if not root:
            return 0
        left = self.longestConsecutiveHelper(root.left)
        right = self.longestConsecutiveHelper(root.right)
        res = 1
        if left > 0 and root.left.val == root.val + 1:
            res = max(res, left + 1)
        if right > 0 and root.right.val == root.val + 1:
            res = max(res, right + 1)
        self.longest = max(self.longest, res)
        return res


"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to 
any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child 
(cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
