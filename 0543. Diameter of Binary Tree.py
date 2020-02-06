# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.depth(root)
        return self.diameter
    
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        self.diameter = max(left + right, self.diameter)
        
        return max(left, right) + 1
    

class Solution1(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root)[1]
    
    def depth(self, root):
        if not root:
            return (0, 0)
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        depth = max(left[0], right[0]) + 1
        diameter = max(left[0] + right[0], left[1], right[1])
        
        return (depth, diameter)
        