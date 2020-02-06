# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion, dfs, preorder, O(n)
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        for child in [root.left, root.right]:
            if child and child.val != root.val:
                return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
    
