# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('inf')
        self.minAndMax(root)
        return self.res
    
    def minAndMax(self, root):
        # return the min and max of values in the tree root
        left_min, right_max = root.val, root.val
        if root.left:
            left_min, left_max = self.minAndMax(root.left)
            self.res = min(self.res, abs(root.val - left_max))
        if root.right:
            right_min, right_max =self.minAndMax(root.right)
            self.res = min(self.res, abs(root.val - right_min))
        return (left_min, right_max)
    
