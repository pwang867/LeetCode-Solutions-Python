# iteration
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        dummy = TreeNode(0)
        pre = dummy
        stack = [root]
        while stack:
            cur = stack.pop()
            pre.left = None
            pre.right = cur
            pre = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        
        dummy.right = None
    


# recursion, different helper with method 1
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(0)
        self.flattenHelper(dummy, root)
        return dummy.right
    
    def flattenHelper(self, parent, root):
        # flatten root and connect to parent, return the last node
        if not root:
            return parent
        parent.right = root
        parent.left = None
        copy = root.right
        if not root.left and not root.right:
            return root
        last_node = self.flattenHelper(root, root.left)
        return self.flattenHelper(last_node, copy)


# recursion
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flattenHelper(root)
        
    
    def flattenHelper(self, root):
        # flatten root and return the head and tail of the flattened list
        if not root:
            return (None, None)
        if not root.left and not root.right:
            return (root, root)
            
        
        left_head, left_tail = self.flattenHelper(root.left)
        right_head, right_tail = self.flattenHelper(root.right)
        
        root.left = None  # don't forget!!!!
        if left_head:
            root.right = left_head
            left_tail.right = right_head
        
        # right_tail and left_tail won't be both None
        return (root, right_tail) if right_tail else (root, left_tail)  


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

