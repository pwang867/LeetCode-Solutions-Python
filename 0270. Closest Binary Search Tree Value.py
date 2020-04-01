# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n)
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1
        ans = float("inf")
        diff = float("inf")
        curr = root
        while curr:
            if abs(target - curr.val)< diff:
                diff = abs(target - curr.val)
                ans = curr.val
            if diff == 0:  # do not return target, return an integer, or do int(target)
                return curr.val
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return ans


"""
Given a non-empty binary search tree and a target value, 
find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value 
in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

