# time O(n)
# space O(height)
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        return self.pathSum(root, limit, 0)
    
    def pathSum(self, root, limit, cur):
        if not root:
            return None
        cur += root.val
        if not root.left and not root.right:
            if cur >= limit:
                return root
            else:
                return None
        root.left = self.pathSum(root.left, limit, cur)
        root.right = self.pathSum(root.right, limit, cur)
        if not root.left and not root.right:
            return None
        else:
            return root


"""
Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]
 

Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]
 

Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
"""
