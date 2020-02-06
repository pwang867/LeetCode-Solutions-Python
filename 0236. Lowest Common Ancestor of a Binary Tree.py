# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 2: carry (p, q, common ancestor) during backtracking
# one pass time O(n), space recursion depth O(depth)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        if left and left is not p and left is not q:   # when left is the ancestor, prune by not going right
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


# method 1: find path from root to p and q, then compare the path
# time O(n), space O(depth)
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        self.ans = []
        self.count = 0
        
        self.findPath(root, p, q, [])
        
        if len(self.ans) == 2:
            left, right = self.ans
        else:
            print "one treenode is not found"
        n = min(len(left), len(right))
        common = None
        for i in range(n):
            if left[i] == right[i]:
                common = left[i]
            else:
                break
        return common
    
    def findPath(self, root, p, q, path):
        if self.count == 2:
            return
        if not root:
            return
        if root == p or root == q:
            self.ans.append(path + [root])
            self.count += 1
        if root.left:
            path.append(root)
            self.findPath(root.left, p, q, path)
            path.pop()
        if root.right:
            path.append(root)
            self.findPath(root.right, p, q, path)
            path.pop()
            


"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
