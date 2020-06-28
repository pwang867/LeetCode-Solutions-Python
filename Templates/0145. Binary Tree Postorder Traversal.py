# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 3, Morris iteration, time O(n), space O(1)
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        dummy = TreeNode(0)
        dummy.left = root
        cur = dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and pre.right is not cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    # reverse path
                    p1, p2 = cur, cur.left
                    while p2 is not cur:
                        copy = p2.right
                        p2.right = p1
                        p1, p2 = p2, copy
                    
                    # update res and reverse back
                    p1, p2 = cur, pre
                    while p2 is not cur:
                        res.append(p2.val)
                        copy = p2.right
                        p2.right = p1
                        p1, p2 = p2, copy
                    
                    # disconnect
                    pre.right = None
                    cur = cur.right
        
        return res


# method 2: stack, iteration, time O(n), space O(height) in balanced tree
class Solution2(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        
        stack = []
        p = root
        pre = None
        
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                p = p.right
                if p is None or p is pre:
                    p = stack.pop()
                    res.append(p.val)
                    pre = p
                    p = None
        
        return res
                

# method 1: using queue, not in topological order of postorder
# kind of cheating
# traverse: node->right->left, and save res in reversed order
from collections import deque
class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # using two stacks
        if not root:
            return []
        
        ans = deque()  
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            ans.appendleft(node.val)               # cheating
        
        return list(ans)



"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted
"""

