# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time O(n), space O(n), recursion, one traverse
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.postorder(root, res)
        return res
    
    def postorder(self, root, res):
        # return max depth of current root
        if not root:
            return -1
        left = self.postorder(root.left, res)
        right = self.postorder(root.right, res)
        depth = max(left, right) + 1   # don't forget + 1
        while len(res) <= depth:
            res.append([])
        res[depth].append(root.val)
        return depth



"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
"""
