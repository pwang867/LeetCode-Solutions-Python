# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 3, Morris, time O(n), space O(1)
class Solution3(object):
    def isSameTree(self, p, q):
        
        def move(p):
            if not p.left:
                p = p.right
            else:
                pre = p.left
                while pre.right and pre.right != p:
                    pre = pre.right
                if not pre.right:
                    pre.right = p
                    p = p.left
                else:
                    pre.right = None
                    p = p.right
            return p
            
        
        while p and q:
            if p.val != q.val:
                return False
            p = move(p)
            q = move(q)
        return not p and not q
            


# method 2, iteration, two stacks, in order, space worst case O(n), time (n)
class Solution(object):
    def isSameTree(self, p, q):
        
        def move(p, stackp):
            if p:
                stackp.append(p)
                p = p.left
            else:
                p = stackp.pop()
                p = p.right
            return p, stackp
        
        stackp = []
        stackq = []
        while (p or stackp) and (q or stackq):
            if (not p and q) or (p and not q):
                return False
            if p and q and p.val != q.val:
                return False
            p, stackp = move(p, stackp)
            q, stackq = move(q, stackq)
        
        if p or stackp or q or stackq:
            return False
        else:  
            return True  # don't forget


# method 1, recursion, space O(n), time O(n)
class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not p:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)



"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

