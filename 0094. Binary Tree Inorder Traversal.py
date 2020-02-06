# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 4: inorder iteration using Morris method
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left  # step 1: go left
                while pre.right and pre.right != cur:  # step 2: all the way right
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    pre.right = None
                    cur = cur.right
        return res



# method 3: inorder iteration using stack
class Solution3(object):
    def inorderTraversal(self, root):
        res = []
        
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        
        return res
    

# method 2: recursion with helper
class Solution2(object):
    def inorderTraversal(self, root):
        self.res = []
        self.inorderHelper(root)
        return self.res
    
    def inorderHelper(self, root):
        if not root:
            return 
        
        self.inorderHelper(root.left)
        self.res.append(root.val)
        self.inorderHelper(root.right)
        
        


# method 1: recursion without helper
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
    
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""
