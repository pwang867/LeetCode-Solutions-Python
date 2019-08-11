# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            (not parent and root not in covered):
            cnt += 1
            covered.update({parent, root, root.left, root.right})
        
        return cnt
    
    
    
#     def minCameraCover(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         covered = {None}
#         cnt = [0]
#         self.minCameraHelper(root, None, covered, cnt)
#         return cnt[0]
    
#     def minCameraHelper(self, root, parent, covered, cnt):
#         if not root:
#             return
        
#         # post order processing
#         self.minCameraHelper(root.left, root, covered, cnt)
#         self.minCameraHelper(root.right, root, covered, cnt)
        
#         if (root.left not in covered) or (root.right not in covered) or \
#             (not parent and root not in covered):
#             cnt[0] += 1
#             covered.update({parent, root, root.left, root.right})
        
