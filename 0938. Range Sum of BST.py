# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 3: iteration, level-wise traversal
class Solution3(object):
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                total += node.val
            if node.val > L and node.left:
                stack.append(node.left)
            if node.val < R and node.right:
                stack.append(node.right)
        return total

    
# method 2: recursion, use BST property
class Solution(object):
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        
        total = 0
        if L <= root.val <= R:
            total += root.val
        if root.val > L:
            total += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            total += self.rangeSumBST(root.right, L, R)
        
        return total


# method 1: recursion, without using property of BST O(n)
class Solution1(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        left = self.rangeSumBST(root.left, L, R)
        right = self.rangeSumBST(root.right, L, R)
        val = root.val if root.val >= L and root.val <= R else 0
        return left + right + val
    
