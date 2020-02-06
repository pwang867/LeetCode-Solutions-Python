# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# preorder iteration, different template
class Solution3(object):
    def maxDepth(self, root):
        p = root
        depth = 1
        max_depth = 0
        stack = []
        while p or stack:
            if p:
                max_depth = max(max_depth, depth)
                stack.append((depth, p))
                p = p.left
                depth += 1
            else:
                depth, p = stack.pop()
                p = p.right
                depth += 1
        return max_depth
    

# preorder iteration
class Solution2(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        max_depth = 0
        stack = [(1, root)]
        while stack:
            depth, node = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((depth+1, node.right))
            if node.left:
                stack.append((depth+1, node.left))
        
        return max_depth


# recursion, space O(n), time O(n)
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
