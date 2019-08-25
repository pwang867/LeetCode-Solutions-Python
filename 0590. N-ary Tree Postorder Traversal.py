"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# iteration
class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        
        res = []
        
        stack = [root]
        pre = root
        while stack:
            p = stack[-1]
            if not p.children or pre in p.children:
                # process p
                stack.pop()
                res.append(p.val)
                pre = p
            else:
                for child in p.children[::-1]:
                    if child:
                        stack.append(child)
        
        return res


# recursion
class Solution1(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.postorderHelper(root, res)
        return res
    
    def postorderHelper(self, root, res):
        if not root:
            return
        
        for child in root.children:
            if child:
                self.postorderHelper(child, res)
        
        res.append(root.val)
        
