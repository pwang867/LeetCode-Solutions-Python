# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Morris


# iteration, stack, similar to postorder-traversal
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        
        p = root
        stack = []   # stack is actually the path
        path = []
        remaining = sum
        pre = None
        while p or stack:
            if p:
                stack.append(p)
                path.append(p.val)
                remaining -= p.val
                p = p.left
            else:
                if not stack[-1].left and not stack[-1].right and remaining == 0:
                    res.append(path[:])
                p = stack[-1].right
                if p is None or p is pre:
                    pre = stack.pop()
                    path.pop()
                    remaining += pre.val
                    p = None
        
        return res


# recursion, DFS
class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.pathSumHelper(root, sum, [], res)
        return res
    
    def pathSumHelper(self, root, remaining, path, res):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == remaining:
                res.append(path + [root.val])
            return
            
        remaining -= root.val
        path.append(root.val)
        if root.left:
            self.pathSumHelper(root.left, remaining, path, res)
        if root.right:
            self.pathSumHelper(root.right, remaining, path, res)
        path.pop()


"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's 
sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
