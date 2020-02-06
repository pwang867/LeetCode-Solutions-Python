# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time O(n), space O(depth)
# we can simply return the sum of children's value

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.postorder(root)
        return self.res
    
    def postorder(self, root):
        # return the sum of children
        if not root:
            return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        if root.val %2 == 0:
            self.res += left+right
        res = 0
        if root.left:
            res += root.left.val
        if root.right:
            res += root.right.val
        return res



"""
Share
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
Accepted
"""
