"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# method 3: iteration
class Solution3(object):
    def preorder(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            for i in range(len(p.children)-1, -1, -1):
                child = p.children[i]
                if child:
                    stack.append(child)
        
        return res


# recursion, with helper function
class Solution2(object):
    def preorder(self, root):
        
        res = []
        self.preorderHelper(root, res)
        return res
    
    def preorderHelper(self, root, res):
        if not root:
            return
        res.append(root.val)
        for child in root.children:
            self.preorderHelper(child, res)
        
    
    
# method 1: recursion
class Solution1(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = [root.val]
        
        for child in root.children:
            res.extend(self.preorder(child))
        
        return res
    
