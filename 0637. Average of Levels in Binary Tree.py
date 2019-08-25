# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# simple level-wise traversal
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        level = [root]
        averages = []
        while level:
            vals = [node.val for node in level]
            averages.append(sum(vals)*1.0/len(vals))
            level = [child for node in level \
                     for child in [node.left, node.right] if child]
        
        return averages
    
