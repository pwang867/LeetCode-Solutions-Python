# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time O(n) for all methods
 
# Morris traversal, travel left subtree in pre-order, while the right subtree in mirrored version
# space O(1)


class Solution5(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        curL, curR = root.left, root.right
        while curL and curR:
            if curL.val != curR.val:
                return False
            # traverse left subtree
            if not curL.left:
                curL = curL.right
            else:
                pre = curL.left
                while pre.right != None and pre.right != curL:
                    pre = pre.right
                if not pre.right:
                    pre.right = curL
                    curL = curL.left
                else:
                    pre.right = None
                    curL = curL.right
            # traverse right subtree in mirror, change curL to curR, .left to .right, and .right to .left
            if not curR.right:
                curR = curR.left
            else:
                pre = curR.right
                while pre.left != None and pre.left != curR:
                    pre = pre.left
                if not pre.left:
                    pre.left = curR
                    curR = curR.right
                else:
                    pre.left = None
                    curR = curR.left
        return not curL and not curR
    

# method 4, DFS, recursion
# recursion depth O(depth)


class Solution4(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isMirror(root1.left, root2.right) \
            and self.isMirror(root1.right, root2.left)


# method 3, DFS, iteration using two stacks
# space O(depth)


class Solution3(object):
    def isSymmetric(self, root):
        if not root:
            return True
        stack1 = [root.left]   # node-left-right
        stack2 = [root.right]  # node-right-left
        while stack1 and stack2:
            p1, p2 = stack1.pop(), stack2.pop()
            if not p1 and not p2:
                continue
            elif not p1 or not p2:
                return False
            else:
                if p1.val != p2.val:
                    return False
            stack1.extend([p1.right, p1.left])
            stack2.extend([p2.left, p2.right])
        return not stack1 and not stack2


# method 2, DFS, iteration, use one stack, save pairs
# space O(depth)


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                stack.append((left.right, right.left))
                stack.append((left.left, right.right))
        return True
    

# method 1, BFS, iteration, level-order
# space O(n)


class Solution1(object):
    def isSymmetric(self, root):
        level = [root]
        while level:
            # check if current level is symmetric using two pointers
            left, right = 0, len(level)-1
            while left < right:
                if not level[left] and not level[right]:
                    left += 1
                    right -= 1
                elif not level[left] or not level[right]:
                    return False
                else:
                    if level[left].val != level[right].val:
                        return False
                    else:
                        left += 1
                        right -= 1
            
            new_level = []
            for node in level:
                if node:
                    new_level.extend([node.left, node.right])
            level = new_level
        
        return True


"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.

Accepted
"""
