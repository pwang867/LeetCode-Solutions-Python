# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level-wise traversal
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        
        level = [(None, root)]
        while level:
            parents = []  # parents of x and y
            for parent, node in level:
                if node.val == x or node.val == y:
                    parents.append(parent)
            if len(parents) == 1:  # only find x or y in current level
                return False
            if len(parents) == 2:
                return parents[0] != parents[1]
            
            level = [(node, child) for parent, node in level \
                     for child in [node.left, node.right] if child]
        
        return False
    
