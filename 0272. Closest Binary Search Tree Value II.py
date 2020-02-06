# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# maintain a sliding window of size k, and terminate early, time < O(n)
from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if k <= 0: return []
        res = deque()   # keep the size of res no more than k
        self.inorder(root, target, k, res)
        return res
    
    def inorder(self, root, target, k, res):
        if not root:
            return
        self.inorder(root.left, target, k, res)
        if len(res) == k:       # maintain a sliding window and early termination
            if abs(root.val - target) < abs(res[0] - target):
                res.popleft()   # don't add extra: res.append(root.val)
            else:
                return
        res.append(root.val)  # don't forget
        self.inorder(root.right, target, k, res)
        
        
        
"""
Given a non-empty binary search tree and a target value, 
find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""
