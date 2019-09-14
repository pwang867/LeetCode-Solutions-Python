# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# divide and conquer
# one of root.left and root.right must be completely filled
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = root, root
        height = 0
        while right: # right edge must reach the end no later than left edge
            right = right.right
            left = left.left
            height += 1
        if not left:  # the tree is completely filled
            return 2**height - 1
        else:
            return self.countNodes(root.left) + 1 + self.countNodes(root.right)
        
        
