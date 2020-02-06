# method 2, use presum, O(n)
from collections import defaultdict
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        pre_sums = defaultdict(int)
        pre_sums[0] = 1  # needs padding !!!, very easy to forget
        return self.helper(root, 0, sum, pre_sums)
    
    def helper(self, root, cur_sum, target, pre_sums):
        if not root:
            return 0
        cur_sum += root.val
        res = pre_sums[cur_sum-target]
        pre_sums[cur_sum] += 1
        res += self.helper(root.left, cur_sum, target, pre_sums) \
                + self.helper(root.right, cur_sum, target, pre_sums)
        pre_sums[cur_sum] -= 1  # backtracking
        return res


# method 1: O(n^2)
class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # This function will make every node in the tree call the function self.helper
        if not root:
            return 0
        return self.helper(root, sum) \
                + self.pathSum(root.right, sum) \
                + self.pathSum(root.left, sum)
        
    def helper(self, node, target):  
        if not node:
            return 0
        return self.helper(node.right, target - node.val) \
                + self.helper(node.left, target - node.val) \
                + int(node.val == target)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range 
-1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
