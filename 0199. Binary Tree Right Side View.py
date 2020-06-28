# BFS, time/space O(n)
class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level = [root]
        ans = []
        
        while level:
            ans.append(level[-1].val)
            level = [child for node in level for child in [node.left, node.right] if child]
        
        return ans


# DFS, mirrored-preorder traversal
class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = {}   # depth: right-most node
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if depth not in res:
                res[depth] = node.val
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return res.values()
    

"""
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
