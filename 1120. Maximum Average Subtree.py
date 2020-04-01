# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        if not root:
            return None
        self.max_avg = -float('inf')
        self.dfs(root)
        return self.max_avg
    
    def dfs(self, root):
        # return (sum, count)
        if not root:
            return (0.0, 0.0)
        left_sum, left_cnt = self.dfs(root.left)
        right_sum, right_cnt = self.dfs(root.right)
        total_sum = left_sum + right_sum + root.val
        total_cnt = left_cnt + right_cnt + 1
        self.max_avg = max(self.max_avg, total_sum/total_cnt)
        return (total_sum, total_cnt)


'''
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

 

Example 1:



Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
 

Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
'''
