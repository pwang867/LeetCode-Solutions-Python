# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time O(n), space O(depth)
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.postOrder(root, None)
    
    def postOrder(self, root, parent):
        if not root:
            return 0
        if not root.left and not root.right \
        and parent and parent.left == root:  # when it is a left leaf
            return root.val
        return self.postOrder(root.left, root) \
                + self.postOrder(root.right, root)


# time O(n), space O(depth)
class Solution1(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #  try recursive first
        if not root:
            return 0
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:  # check if root.left is a leaf
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        if root.right:
            # if not root.right.left and not root.right.right:  # wrong codes: right leaf doesn't count !!!
            #     ans += root.right.val
            # else:
            #     ans += self.sumOfLeftLeaves(root.right)
            ans += self.sumOfLeftLeaves(root.right)
        return ans


"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
