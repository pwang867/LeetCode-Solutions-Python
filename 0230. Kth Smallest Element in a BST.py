# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# follow up, when the BST tree changes and the BST tree is changed often
# we will store counts in the tree node
class MyTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1
    
class Solution(object):
    def kthSmallest(self, root, k):
        my_root = self.buildMyTree(root)
        return self.kthSmallestHelper(my_root, k)
    
    def buildMyTree(self, root):
        # change TreeNode to myTreeNode, and return a MyTreeNode
        if not root:
            return None
        
        my_root = MyTreeNode(root.val)
        my_root.left = self.buildMyTree(root.left)
        my_root.right = self.buildMyTree(root.right)
        if my_root.left:
            my_root.count += my_root.left.count
        if my_root.right:
            my_root.count += my_root.right.count
        
        return my_root
    
    def kthSmallestHelper(self, root, k):
        # search kth smallest value in MyTreeNode tree
        if not root or k == 0:
            return None
        left_cnt = root.left.count if root.left else 0
        if left_cnt == k-1:
            return root.val
        if left_cnt > k-1:
            return self.kthSmallestHelper(root.left, k)
        else:
            return self.kthSmallestHelper(root.right, k - left_cnt - 1)


# method 2: count the number of nodes in the BST
# time O(n), not O(n*log(n))
class Solution2(object):
    def kthSmallest(self, root, k):
        if not root:
            return None
        n = self.count(root.left)
        if n == k-1:
            return root.val
        if n >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-1-n)
        
    
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
        
            



# method 1: inorder search, and stops when k elements are found
class Solution1(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.inorder(root, res, k)
        return res[k-1]
    
    def inorder(self, root, res, k):
        if not root:
            return
        if len(res) >= k:
            return
        self.inorder(root.left, res, k)
        res.append(root.val)
        self.inorder(root.right, res, k)


