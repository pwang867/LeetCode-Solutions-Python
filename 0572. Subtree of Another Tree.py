# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 2, iteration, time O(n*m), space O(n+m)
# time complexity can be optimized to O(m+n) using KMP pattern match


class Solution(object):
    def isSubtree(self, s, t):
        s_list = self.preorderSerialize(s)
        t_list = self.preorderSerialize(t)
        
        for i in range(len(s_list)-len(t_list)+1):
            if s_list[i:i+len(t_list)] == t_list:
                return True
        
        return False
    
    def preorderSerialize(self, s):
        # preorder serialization of a tree
        res = []
        stack = []
        p = s
        while stack or p:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                res.append(None)  # easy to miss
                p = stack.pop()
                p = p.right
        res.append(None)  # easy to miss, the last empty node is not recorded yet
        return res


# method 1, recursion, time O(n*m), space O(n) stack memory


class Solution1(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return not t
        if not t:
            return True
        
        if self.isSame(self, s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self, s, t):
        # check if s and t are the same tree, 
        # each corresponding node has the same value
        if not s:
            return not t
        if not t:
            return False
        
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
    

"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values 
with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

