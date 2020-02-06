# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time O(n)
from collections import deque
class Solution(object):
    def __init__(self):
        self.res = []
        
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        voyage = deque(voyage)
        self.dfs(root, voyage)
        return self.res
    
    def dfs(self, root, voyage):
        if not root:
            return True
        val = voyage.popleft()
        if root.val != val:
            self.res = [-1]
            return False
        else:
            if root.left and root.left.val != voyage[0]:  # need flip
                self.res.append(val)
                root.left, root.right = root.right, root.left
            if not self.dfs(root.left, voyage):
                return False
            if not self.dfs(root.right, voyage):
                return False
            return True
        

# method 1, O(n^3)
class Solution1(object):
    
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if not root or not voyage:
            return []
        self.memo = {}
        can_flip, nodes = self.helper(root, voyage, 0, len(voyage)-1)
        if can_flip:
            return nodes
        else:
            return [-1]
    
    def helper(self, root, voyage, left, right):
        if not root:
            return [right < left, []]
        if right < left:
            return [False, []]
        if root.val != voyage[left]:
            return [False, []]
        if left == right:
            return [not root.left and not root.right, []]
        if not root.left and not root.right:
            return [left==right, []]
        key = (root.val, left, right)
        if key in self.memo:
            return self.memo[key]
        if not root.left:
            root.left, root.right = root.right, root.left
        if root.left.val == voyage[left+1]:
            for end in range(left, right+1):
                left_can, left_nodes = self.helper(root.left, voyage, 
                                                   left+1, end)
                if not left_can:
                    continue
                right_can, right_nodes = self.helper(root.right, voyage, 
                                                     end+1, right)
                if left_can and right_can:
                    self.memo[key] = [True, left_nodes + right_nodes]
                    return self.memo[key]
        else:
            for end in range(left, right+1):
                left_can, left_nodes = self.helper(root.left, voyage, 
                                                   end+1, right)
                if not left_can:
                    continue
                right_can, right_nodes = self.helper(root.right, voyage, 
                                                     left+1, end)
                if left_can and right_can:
                    self.memo[key] = [True, [root.val]+left_nodes+right_nodes]
                    return self.memo[key]
        self.memo[key] = [False, []]
        return self.memo[key]


"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:



Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:



Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:



Input: root = [1,2,3], voyage = [1,2,3]
Output: []
 

Note:

1 <= N <= 100
"""
