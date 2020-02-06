# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 4, Morris, time O(n), space O(1)
class Solution4(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:  # revisit cur, don't update res
                    pre.right = None
                    cur = cur.right
        
        return res


# method 3: iteration, stack
# time O(n), space O(log(n)) average, worst case O(n)
class Solution3(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        
        stack = []
        p = root
        while stack or p:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        
        return res


# recursion, with helper function
class Solution2(object):
    def preorderTraversal(self, root):
        
        res = []
        self.preorderHelper(root, res)
        return res
    
    def preorderHelper(self, root, res):
        if not root:
            return
        res.append(root.val)
        for child in [root.left, root.right]:
            self.preorderHelper(child, res)

    
# recursion, no helper function
class Solution1(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res


"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
