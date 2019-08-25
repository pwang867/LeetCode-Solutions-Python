"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# levelwise traversal is fit for iteration instead of recursion
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        level = [root]
        while level:
            vals = []
            new_level = []
            for node in level:
                vals.append(node.val)
                for child in node.children:
                    if child:
                        new_level.append(child)
            res.append(vals)
            level = new_level
        
        return res
    

# recursion
class Solution1(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        self.levelOrderHelper(root, 0, res)
        return res
    
    def levelOrderHelper(self, root, level, res):
        if not root:
            return
        
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        
        for child in root.children:
            if child:
                self.levelOrderHelper(child, level+1, res)
        
