# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# root to leaf


# time/space O(res)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        res = []
        self.dfs(root, [], res)
        return res
    
    def dfs(self, root, path, res):
        if not root: return
        path.append(str(root.val))
        if not root.right and not root.left:
            res.append("->".join(path))
        if root.left:
            self.dfs(root.left, path, res)
        if root.right:
            self.dfs(root.right, path, res)
        path.pop()
        

# time/space O(res)
class Solution1(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        if not root:
            return ans
        if not root.left and not root.right:
            return [str(root.val)]
        
        if root.left:
            ans_left = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        else:
            ans_left = []
        if root.right:
            ans_right = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]
        else:
            ans_right = []
        
        return ans_left + ans_right



"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
