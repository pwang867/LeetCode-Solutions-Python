# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        
        arr = [i for i in range(1, n+1)]
        return self.BSTHelper(arr, 0, n-1)
    
    def BSTHelper(self, arr, low, high):
        if low > high:
            return [None]
        
        trees = []
        for i in range(low, high+1):
            left_trees = self.BSTHelper(arr, low, i-1)
            right_trees = self.BSTHelper(arr, i+1, high)
            for ltree in left_trees:
                for rtree in right_trees:
                    root = TreeNode(arr[i])
                    root.left = ltree
                    root.right = rtree
                    trees.append(root)
        
        return trees
    
