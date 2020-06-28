# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# iteration, time O(n), extra space worst O(n) except the tree itself


class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        # the following four variables will be updated frequently
        stack = [root]   
        pre = None  # to control going left or right, pre=None (go left), pre != None (go right)
        p = 1
        i = 0  # inorder is used to tell if we can still go left
        
        while p < len(preorder):
            if stack and stack[-1].val == inorder[i]:  # can not go left anymore
                pre = stack.pop()
                i += 1
            elif pre:   # go right
                node = TreeNode(preorder[p])
                pre.right = node
                stack.append(node)
                p += 1
                pre = None
            else:   # go left
                node = TreeNode(preorder[p])
                stack[-1].left = node
                stack.append(node)
                p += 1
        
        return root
    

# recursion, time O(n), space O(1)


class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # input check ignored: set(preorder) == set(inorder)
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        return self.buildTreeHelper(preorder, 0, inorder, 0, len(preorder), inorder_dict)
    
    def buildTreeHelper(self, preorder, pre_start, inorder, in_start, length, inorder_dict):
        # inorder argument can be removed since it's not used
        if length <= 0:
            return None
        if length == 1:
            return TreeNode(preorder[pre_start])
        val = preorder[pre_start]
        root = TreeNode(val)
        i = inorder_dict[val]
        left_len = i - in_start
        root.left = self.buildTreeHelper(preorder, pre_start+1, inorder, in_start, 
                                         left_len, inorder_dict)
        root.right = self.buildTreeHelper(preorder, pre_start+left_len+1, inorder, i+1, 
                                          length-left_len-1, inorder_dict)
        return root


"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

