# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteration, in order traversal
class Solution(object):
    def minDiffInBST(self, root):
        if not root:
            return 0
        
        stack = []  # store the path
        node = root  # to be processed
        res = float('inf')
        pre = -float('inf')
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # every node before the popped node is already processed
                # in order traversal
                node = stack.pop()  
                res = min(res, node.val - pre)
                pre = node.val  # do not forget!!
                node = node.right
        return res
    

# recursion, O(n)
# return the min and max of a root
class Solution1(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('inf')
        self.minAndMax(root)
        return self.res
    
    def minAndMax(self, root):
        # return the min and max of values in the tree root
        left_min, right_max = root.val, root.val
        if root.left:
            left_min, left_max = self.minAndMax(root.left)
            self.res = min(self.res, abs(root.val - left_max))
        if root.right:
            right_min, right_max =self.minAndMax(root.right)
            self.res = min(self.res, abs(root.val - right_min))
        return (left_min, right_max)
    
