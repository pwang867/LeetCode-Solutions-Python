# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# iteration, pre-order
# watch out: the value of children may be equal to the parent
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        minimum = root.val
        second = float('inf')  # second minimum
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != minimum:
                second = min(second, node.val)
            else:
                stack.append(node.right)
                stack.append(node.left)
        
        return second if second != float('inf') else -1
    
