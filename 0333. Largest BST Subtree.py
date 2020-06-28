# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time O(n), space O(depth) due to recursion


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_size = 0
        self.helper(root)
        return self.max_size

    def helper(self, root):
        if not root:
            return (True, None, None, 0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left[0] or not right[0]:
            return (False, 0, 0, 0)
        if left[2] is not None and left[2] >= root.val:  # mistake: left[2] > root.val
            return (False, 0, 0, 0)
        if right[1] is not None and right[1] <= root.val:
            return (False, 0, 0, 0)
        low = left[1] if left[1] is not None else root.val
        high = right[2] if right[2] is not None else root.val
        cnt = left[3] + right[3] + 1
        self.max_size = max(self.max_size, cnt)
        return (True, low, high, cnt)


if __name__ == "__main__":
    root = TreeNode(10)
    s = Solution()
    res = s.largestBSTSubtree(root)
    print(res)
    print(s.max_size)

"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), 
where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
