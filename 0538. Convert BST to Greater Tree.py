# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 3, Morris traversal, time O(n), space O(1)

class Solution3(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0
        cur = root
        while cur:
            if not cur.right:
                cur.val += total
                total = cur.val
                cur = cur.left
            else:
                pre = cur.right
                while pre.left != None and pre.left != cur:
                    pre = pre.left
                if pre.left is None:
                    pre.left = cur
                    cur = cur.right
                else:
                    cur.val += total
                    total = cur.val
                    pre.left = None
                    cur = cur.left
        return root

    

'''
method 2
reverse inorder traversal
time O(n), space O(height)
'''

class Solution2(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        p = root
        total = 0
        while stack or p:
            if p:
                stack.append(p)
                p = p.right
            else:
                p = stack.pop()
                p.val += total
                total = p.val
                p = p.left
        return root


# recursion
class Solution1(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        self.dfs(root)
        return root
    
    def dfs(self, root):
        # reverse inorder
        if not root:
            return
        self.dfs(root.right)
        root.val += self.total
        self.total = root.val
        self.dfs(root.left)
        


"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that 
every key of the original BST is changed to the original key plus sum of 
all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""
