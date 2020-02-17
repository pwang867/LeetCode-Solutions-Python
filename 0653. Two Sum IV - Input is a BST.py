# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 3, use hashset
# time O(n), space O(n)
class Solution3(object):
    def findTarget(self, root, k):
        if not root:
            return False
        
        seen = set()
        stack= [root]
        while stack:  # preorder traversal
            node = stack.pop()
            if k - node.val in seen:
                return True
            else:
                seen.add(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return False


# method 2, tranfer the BST into an ordered array, 
# and then use methods in regular Two Sum
# time O(n), space O(n) for storing the array
class Solution2(object):
    def findTarget(self, root, k):
        arr = []
        self.BSTToArray(root, arr)
        
        left, right = 0, len(arr)-1
        while left < right:
            temp = arr[left] + arr[right]
            if temp == k:
                return True
            elif temp > k:
                right -= 1
            else:
                left += 1
        return False      
    
    
    def BSTToArray(self, root, arr):
        # tranfer BST to an inorder array
        if not root:
            return
        self.BSTToArray(root.left, arr)
        arr.append(root.val)
        self.BSTToArray(root.right, arr)
        

# method 1, iterate every node in the BST, and search its pair in the whole tree
# time O(n*depth), space O(depth) for stack and recursion
class Solution1(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def search(root, y):  
            # return: boolean
            # this function searches the node with value y
            if not root:
                return False
            if root.val == y:
                return True
            elif root.val > y:
                return search(root.left, y)
            elif root.val < y:
                return search(root.right, y)
            
        
        if not root:
            return False
        stack = [root]
        
        while stack:  # use stack for pre-order traversal
            node = stack.pop()
            if node.val*2 > k and search(node.left, k - node.val):
                return True
            if 2*node.val < k and search(root, k - node.val):  
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        
        return False
    

"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
