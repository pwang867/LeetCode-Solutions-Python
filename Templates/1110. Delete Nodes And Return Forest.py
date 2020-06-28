# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 2, based on method 1, but the edge cutting is much smarter
# time O(n), space O(depth), and save forest (O(n))
# idea: if a node has no parent and is not deleted, then add to the forest


class Solution2(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)
        forest = []
        self.delNodesHelper(None, root, to_delete, forest)
        return forest
    
    def delNodesHelper(self, parent, root, to_delete, forest):
        if not root:
            return None
        
        if root.val in to_delete:   # this block of codes can be simplified to make code cleaner
            root.left = self.delNodesHelper(None, root.left, to_delete, forest)
            root.right = self.delNodesHelper(None, root.right, to_delete, forest)
            return None  # important: this will cut connection of root with its parent, but not with its children
        else:
            if not parent:
                forest.append(root)
            root.left = self.delNodesHelper(root, root.left, to_delete, forest)
            root.right = self.delNodesHelper(root, root.right, to_delete, forest)
            return root


# add candidates from parent level
class Solution1(object):
    def delNodes(self, root, to_delete):
        candidates = []
        to_delete = set(to_delete)
        if root and root.val not in to_delete:
            candidates.append(root)
        self.trim(None, root, to_delete, candidates)
        return candidates

    def trim(self, parent, root, to_delete, candidates):
        if not root:
            return
        if root.val not in to_delete:
            self.trim(root, root.left, to_delete, candidates)
            self.trim(root, root.right, to_delete, candidates)
        else:
            # store candidates
            if root.left and root.left.val not in to_delete:
                candidates.append(root.left)
            if root.right and root.right.val not in to_delete:
                candidates.append(root.right)
            # cut edge with parent
            if parent:
                if parent.left is root:
                    parent.left = None
                else:
                    parent.right = None
            # cut edge with children
            left = root.left
            right = root.right
            root.left = None
            root.right = None
            self.trim(None, left, to_delete, candidates)
            self.trim(None, right, to_delete, candidates)


"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
