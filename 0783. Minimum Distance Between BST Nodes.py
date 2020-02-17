# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteration, in order traversal, time: O(n), space O(depth)
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


# method 2: recursion, in order traversal
class Solution2(object):
    def minDiffInBST(self, root):
        self.res = float('inf')
        self.pre = -float('inf')
        self.BSTHelper(root)
        return self.res
    
    def BSTHelper(self, root):
        if not root:
            return
        
        self.BSTHelper(root.left)
        
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        
        self.BSTHelper(root.right)


# recursion, post-order, O(n)
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
    

"""
Given a Binary Search Tree (BST) with the root node root, 
return the minimum difference between the values of 
any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 
and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, 
and each node's value is different.
"""
