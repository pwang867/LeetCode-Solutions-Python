# one pass, O(n) time, O(1) space
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        p1, p2, p3 = root, root.left, root.right
        p1.left, p1.right = None, None  # easy to forget
        while p2:
            copy1, copy2 = p2.left, p2.right
            p2.left = p3
            p2.right = p1
            p1, p2, p3 = p2, copy1, copy2
        return p1

# method 2, use stack, and start from new root
# time O(n), space O(n)

"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
"""
