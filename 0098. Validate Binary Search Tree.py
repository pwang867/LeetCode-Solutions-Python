# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 5: in order, iteration, Morris
# time O(n), Morris time O(n), space O(1)
class Solution(object):
    def isValidBST(self, root):
        cur = root
        res = float('inf')
        last = -float('inf')
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    # to create or check a Morris node
                    pre = pre.right
                if not pre.right:  
                    pre.right = cur
                    cur = cur.left
                else: 
                    # a Morris connection is found
                    # cur was visited and now we return to this node
                    pre.right = None  # break the Morris connection
                    if cur.val <= last:
                        return False
                    last = cur.val
                    cur = cur.right
            else:
                # don't break the Morris connection here
                if cur.val <= last:
                    return False
                last = cur.val
                cur = cur.right
        return True
    
        
# method 4: in order, iteration
# time O(n), space O(log(n))
class Solution4(object):
    def isValidBST(self, root):
        if not root:
            return True
        
        stack = []
        node = root
        pre = -float('inf')
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if pre >= node.val:
                    return False
                pre = node.val
                node = node.right
        return True


# method 3: transfer BST to an array and then validate the array
# time O(n), space O(n)
class Solution3(object):
    def isValidBST(self, root):
        arr = []
        self.BSTToArray(root, arr)
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
        
    def BSTToArray(self, root, arr):
        if not root:
            return
        self.BSTToArray(root.left, arr)
        arr.append(root.val)
        self.BSTToArray(root.right, arr)
        

# method 2, simpler recursion, use a boundary (low, high)
# inorder, preorder or postorder are all OK, preoder prefered to be faster
class Solution2(object):
    def isValidBST(self, root):
        if not root:
            return True
        return self.BSTHelper(root, -float('inf'), float('inf'))
    
    def BSTHelper(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.BSTHelper(root.left, low, root.val) and \
                self.BSTHelper(root.right, root.val, high)

# method 1, recursion, return (min, max, isBST)
# time O(n), space O(log(n))
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        ans = self.helper(root)
        return ans[2]
    
    def helper(self, root):
        if not root.left and not root.right:
            return [root.val, root.val, True]
        left_min, right_min, left_valid = float("inf"), float("inf"), True
        left_max, right_max, right_valid = float("-inf"), float("-inf"), True
        if root.left:
            left_min, left_max, left_valid = self.helper(root.left)
        if root.right:
            right_min, right_max, right_valid = self.helper(root.right)
            
        if left_valid and right_valid and (left_max < root.val < right_min):
            is_valid = True
        else:
            is_valid = False
            
        curr_min = min(left_min, right_min, root.val)
        curr_max = max(left_max, right_max, root.val)
        return curr_min, curr_max, is_valid
    
