# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        forest = {root}
        self.delNodesHelper(None, root, to_delete, forest)
        return list(forest)
    
    def delNodesHelper(self, parent, root, to_delete, forest):
        if not root:
            return
        
        if root.val in to_delete:
            if root in forest:  # don't forget to delete for this condition
                forest.remove(root)
            if parent:  # cut root from its parent
                if parent.left == root:
                    parent.left = None
                else:
                    parent.right = None
            if root.left:
                forest.add(root.left)
                self.delNodesHelper(None, root.left, to_delete, forest)
                root.left = None
            if root.right:
                forest.add(root.right)
                self.delNodesHelper(None, root.right, to_delete, forest)
                root.right = None
        else:
            if root.left:
                self.delNodesHelper(root, root.left, to_delete, forest)
            if root.right:
                self.delNodesHelper(root, root.right, to_delete, forest)
        
        
            
