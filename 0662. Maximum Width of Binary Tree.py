# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            ileft, iright = queue[0][1], queue[-1][1]
            maxWidth = max(maxWidth, iright-ileft+1)
            for _ in range(len(queue)):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*i))   # the index in a full binary tee
                if node.right:
                    queue.append((node.right, 2*i+1))
        return maxWidth



"""
662. Maximum Width of Binary Tree
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
"""

