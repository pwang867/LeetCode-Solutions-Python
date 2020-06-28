# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 2, simply use yield


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.it = self.dfs(root)
        self.val = next(self.it) if root else None
    
    def dfs(self, root):
        p = root
        stack = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                yield p.val
                p = p.right

    def next(self):
        res = self.val
        try:
            self.val = next(self.it)
        except:
            self.val = None
        return res
        
    def hasNext(self):
        return self.val != None


# method 1: use stack, move step by step


class BSTIterator1(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []  # space O(log(n)), or called O(h)
        self._travel_leftmost(root)
    
    def _travel_leftmost(self, node):  # time O(log(n))
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self):  # time O(1) on average, one into stack and one pop out
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.stack:
            return -1
        
        node = self.stack.pop()
        val = node.val
        
        node = node.right
        self._travel_leftmost(node)
        
        return val
        

    def hasNext(self):  # tiue O(1)
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
