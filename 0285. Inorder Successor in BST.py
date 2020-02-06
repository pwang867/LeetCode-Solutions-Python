# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 2, recursion, time/space O(depth)
class Solution():
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left or root  # equal: return left if left else root


# method 1, iteration, time O(depth), space O(1)
class Solution1(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        # if p has a right child, then the smallest node in the right subtree will be successor
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        # search from root to p, the last node that turns left will be the successor
        res = None
        cur = root
        while cur:
            if cur is p:
                break
            if cur.val < p.val:
                cur = cur.right
            elif cur.val > p.val:  # turn left
                res = cur
                cur = cur.left
        return res

"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""
