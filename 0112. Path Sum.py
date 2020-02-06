# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 3, Morris traversal, time O(n), space O(1)
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        cur = root
        path = 0   # the path sum from root to cur
        while cur:
            if not cur.left:
                path += cur.val
                if not cur.right and path == sum:
                    return True
                cur = cur.right
            else:
                pre = cur.left
                total = pre.val
                while pre.right and pre.right is not cur:
                    pre = pre.right
                    total += pre.val 
                if pre.right is None:
                    path += cur.val
                    if pre.left is None and path + total == sum:
                        return True
                    pre.right = cur
                    cur = cur.left
                else:
                    path -= total
                    pre.right = None
                    cur = cur.right
        return False
    

# recursion, dfs, preorder
class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:  
            # when the node is a leaf and matches sum
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) \
                   or self.hasPathSum(root.right, sum - root.val)

# iteration, DFS, pre-order, using stack, time O(n), space O(n)
class Solution1(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        stack = [(root, sum)]
        while stack:
            node, total = stack.pop()
            if not node.left and not node.right and node.val == total:
                return True
            total -= node.val
            if node.right:
                stack.append((node.right, total))
            if node.left:
                stack.append((node.left, total))
            
        return False


"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

