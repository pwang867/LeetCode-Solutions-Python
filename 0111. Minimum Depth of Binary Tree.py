# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS, time O(n), space O(n)
from collections import deque
class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        

# recursion, DFS, postorder
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:   # tricky here, unlike max depth of tree
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
