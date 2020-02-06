# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# basic level-wise traversal
# use deque() to save results
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = deque()
        
        level = [root]
        while level:
            ans.appendleft([node.val for node in level])
            level = [child for node in level \
                     for child in [node.left, node.right] if child]
        
        return ans
    

"""
Given a binary tree, return the bottom-up level order traversal of 
its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
