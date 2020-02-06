# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 2: O(n)
class Solution(object):
    def rob(self, root):
        return max(self.robHelper(root))
    
    def robHelper(self, root):
        # return (profit when root robbed, root not robbed)
        if not root:
            return (0, 0)
        left = self.robHelper(root.left)
        right = self.robHelper(root.right)
        return (root.val + left[1] + right[1], max(left) + max(right))
    

# Method 1: O(n) with memo, O(n^n ???) without memo (time limit exceeded) 
class Solution1(object):
    def __init__(self):
        self.memo = {}
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root in self.memo:
            return self.memo[root]
        
        if not root:
            return 0
        res = 0
        
        # if root is not robbed
        right = self.rob(root.right)
        left = self.rob(root.left)
        res = max(res, left + right)
        
        # if root is robbed
        if root.right:
            right1 = self.rob(root.right.right)
            right2 = self.rob(root.right.left)
        else:
            right1 = 0
            right2 = 0
        if root.left:
            left1 = self.rob(root.left.right)
            left2 = self.rob(root.left.left)
        else:
            left1 = 0
            left2 = 0
        res = max(res, root.val + left1 + left2 + right1 + right2)
        
        self.memo[root] = res
        
        return res
    
