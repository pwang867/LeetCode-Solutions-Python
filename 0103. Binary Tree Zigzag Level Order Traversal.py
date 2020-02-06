# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = [root]
        zigzag = []
        left_to_right = True
        
        while level:
            if left_to_right:
                vals = [node.val for node in level]
            else:
                vals = [level[i].val for i in range(len(level)-1, -1, -1)]
            zigzag.append(vals)
            level = [child for node in level for child in [node.left, node.right] if child]
            left_to_right = not left_to_right
        
        return zigzag



"""
Created on Fri Oct 11 21:34:29 2019

@author: WEIMIN ZHOU
"""


"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""