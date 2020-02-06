# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method2, based on method1, but take care of the edge cutting much better
# time O(n), space O(n) for recursion depth, and save forest (O(n))
# idea: if a node has no parent and is not deleted, then add to the forest
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        forest = []
        self.delNodesHelper(None, root, to_delete, forest)
        return forest
    
    def delNodesHelper(self, parent, root, to_delete, forest):
        if not root:
            return None
        
        if root.val in to_delete:
            root.left = self.delNodesHelper(None, root.left, to_delete, forest)
            root.right = self.delNodesHelper(None, root.right, to_delete, forest)
            return None  # this will cut root from its parent, but not from children
        else:
            if not parent:
                forest.append(root)
            root.left = self.delNodesHelper(root, root.left, to_delete, forest)
            root.right = self.delNodesHelper(root, root.right, to_delete, forest)
            return root
        



class Solution1(object):
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
            return None
        
        if root.val in to_delete:
            if root in forest:  # don't forget to delete for this condition
                forest.remove(root)
            if parent:  # cut connection with its parent
                if parent.left == root:  
                    parent.left = None  # necessary
                else:
                    parent.right = None
            if root.left:  # recur for children
                node = root.left
                root.left = None  # not necessary 
                forest.add(node)
                self.delNodesHelper(None, node, to_delete, forest)
            if root.right:
                node = root.right
                root.right = None
                forest.add(node)
                self.delNodesHelper(None, node, to_delete, forest)
        else:
            if root.left:
                self.delNodesHelper(root, root.left, to_delete, forest)
            if root.right:
                self.delNodesHelper(root, root.right, to_delete, forest)
        
        
            