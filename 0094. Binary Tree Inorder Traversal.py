# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 4: inorder iteration using Morris method
# time O(n), space O(1)
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    pre.right = None
                    cur = cur.right
            else:
                res.append(cur.val)
                cur = cur.right
        return res
    


# method 3: inorder iteration using stack
# time O(n), space O(log(n))
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
    
