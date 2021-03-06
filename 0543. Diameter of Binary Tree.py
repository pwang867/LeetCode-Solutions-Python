# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time O(n), space O(depth)
# same as method 1, but use attributes
# diameter: count of edges, not count of nodes
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
    

# method 1, recursion
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


"""
Given a binary tree, you need to compute the length of the diameter 
of the tree. The diameter of a binary tree is the length of the 
longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
        