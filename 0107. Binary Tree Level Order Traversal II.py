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
    
