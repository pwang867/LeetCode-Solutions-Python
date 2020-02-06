# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# method 1: recursion
class Solution1(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        
        return self.BSTHelper(1, n)
    
    def BSTHelper(self, low, high):
        if low > high:
            return [None]
        
        trees = []
        for i in range(low, high+1):
            left_trees = self.BSTHelper(low, i-1)
            right_trees = self.BSTHelper(i+1, high)
            for ltree in left_trees:
                for rtree in right_trees:
                    root = TreeNode(i)
                    root.left = ltree
                    root.right = rtree
                    trees.append(root)
        
        return trees


# method 2: dp, add integers one by one
import copy
class Solution(object):
    def generateTrees(self, n):
        if n <= 0:
            return []
        
        dp = [TreeNode(1)]
        for i in range(2, n+1):  # i will be large than all node values generated before
            new_dp = []
            for node in dp:
                # make TreeNode(i) as root
                root1 = TreeNode(i)
                root1.left = node
                new_dp.append(root1)
                # insert TreeNode(i) as a child node
                for k in range(i):  # tricky here, we should try every right node along the right contour!!
                    root2 = copy.deepcopy(node)  # must deep copy
                    cur = root2
                    for _ in range(k):
                        if cur:
                            cur = cur.right
                        else:
                            break
                    if not cur:
                        break
                    new_node = TreeNode(i)  
                    new_node.left = cur.right
                    cur.right = new_node
                    new_dp.append(root2)
            dp = new_dp
        return dp


"""
Given an integer n, generate all structurally unique BST's 
(binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Accepted
"""
