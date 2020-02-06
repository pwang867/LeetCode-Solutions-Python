"""
Operations on trees:

450. Delete Node in a BST
617. Merge Two Binary Trees
700. Search in a Binary Search Tree
701. Insert into a Binary Search Tree
776. Split BST
"""

# iteration, use two dummy nodes
# for small tree, always grow on the right, and vice versa for the large tree
class Solution(object):
    def splitBST(self, root, V):
        if not root:
            return [None, None]
        dummy_small = TreeNode(0)
        dummy_large = TreeNode(1)
        small, large = dummy_small, dummy_large
        
        cur = root
        while cur:
            if cur.val == V:
                small.right = cur
                small = small.right
                large.left = cur.right
                large = large.left
                cur.right = None
                break
            elif cur.val < V:
                small.right = cur
                small = small.right
                cur = cur.right
                small.right = None
            else:
                large.left = cur
                large = large.left
                cur = cur.left
                large.left = None
        
        return [dummy_small.right, dummy_large.left]




# recursion ,and, return [smaller value tree, large tree]
# time O(height), recursion depth O(height)
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        
        if root.val == V:
            rtree = root.right
            root.right = None
            return [root, rtree]
        elif root.val < V:  # mistake: if root.val > V
            ltree, rtree = self.splitBST(root.right, V)
            root.right = ltree
            return [root, rtree]
        else:
            ltree, rtree = self.splitBST(root.left, V)
            root.left = rtree
            return [ltree, root]



"""
Given a Binary Search Tree (BST) with root node root, and a target value V, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value.  It's not necessarily the case that the tree contains a node with value V.

Additionally, most of the structure of the original tree should remain.  Formally, for any child C with parent P in the original tree, if they are both in the same subtree after the split, then node C should still have the parent P.

You should output the root TreeNode of both subtrees after splitting, in any order.

Example 1:

Input: root = [4,2,6,1,3,5,7], V = 2
Output: [[2,1],[4,3,6,null,null,5,7]]
Explanation:
Note that root, output[0], and output[1] are TreeNode objects, not arrays.

The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

          4
        /   \
      2      6
     / \    / \
    1   3  5   7

while the diagrams for the outputs are:

          4
        /   \
      3      6      and    2
            / \           /
           5   7         1
"""

