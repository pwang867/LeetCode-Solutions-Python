# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 2: stack, iteration
class Solution(object):
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
            ans.appendleft(node.val)
        
        return list(ans)
    
