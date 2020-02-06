# 1. always use postorder numbers to construct the tree
# 2. keep going right as far as possible, and use inorder elements to determine we reaches rightmost node
# 3. use pre to indicate if the last step is going left, go right when pre is None, otherwise go left

# iteration
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(float('inf'))
        stack = [dummy]
        pre, cur = None, dummy
        i, p = len(inorder)-1, len(postorder)-1
        
        while i >= 0:
            if stack[-1].val == inorder[i]:
                pre = stack.pop()
                i -= 1
            elif pre:  # pre is used to determine if the next step is going right or left
                cur = TreeNode(postorder[p]);
                pre.left = cur
                stack.append(cur)
                pre = None  # go left for only one step, then go right
                p -= 1
            else:
                cur = TreeNode(postorder[p]);
                stack[-1].right = cur;
                stack.append(cur)
                p -= 1
        
        return dummy.right
    

# recursion
class Solution1(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        in_dict = {val: i for i, val in enumerate(inorder)}
        return self.buildTreeHelper(inorder, 0, postorder, 0, len(inorder), in_dict)
    
    def buildTreeHelper(self, inorder, in_left, postorder, p_left, length, in_dict):
        if length <= 0:
            return None
        if length == 1:
            return TreeNode(postorder[p_left])
        
        val = postorder[p_left + length - 1]
        i = in_dict[val]
        left_len = i - in_left
        root = TreeNode(val)
        root.left = self.buildTreeHelper(inorder, in_left, postorder, p_left, left_len, in_dict)
        root.right = self.buildTreeHelper(inorder, i+1, postorder, p_left+left_len, 
                                          length-left_len-1, in_dict)
        
        return root
    


"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

