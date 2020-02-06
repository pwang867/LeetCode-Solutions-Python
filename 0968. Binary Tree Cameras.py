# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# greedy, mount camera in the parent's node as much as possible
# time/space O(n)

class Solution(object):
    # solution 2: do not use cnt = [0]
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        covered = {None}
        
        return self.minCameraHelper(root, None, covered)
    
    def minCameraHelper(self, root, parent, covered):
        if not root:
            return 0
        
        # post order processing
        cnt = self.minCameraHelper(root.left, root, covered)
        cnt += self.minCameraHelper(root.right, root, covered)
        
        # parent always have higher precedence than its children
        if (root.left not in covered) or (root.right not in covered) or \
            (not parent and root not in covered):   # easy to miss: (not parent and root not in covered)
            cnt += 1
            covered.update({parent, root, root.left, root.right})
        
        return cnt
    
    

"""
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""
