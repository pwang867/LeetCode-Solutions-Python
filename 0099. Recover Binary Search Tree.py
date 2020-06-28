# method 2, Morris traversal, constant space


# method 4: Morris iteration
class Solution(object):
    def recoverTree(self, root):
        bad_node1, bad_node2 = None, None
        last = None
        cur = root
        while cur:
            print(cur.val)
            if not cur.left:
                if last and last.val > cur.val:
                    bad_node2 = cur
                    if not bad_node1:
                        bad_node1 = last
                last = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    if last and last.val > cur.val:
                        bad_node2 = cur
                        if not bad_node1:
                            bad_node1 = last
                    last = cur
                    pre.right = None
                    cur = cur.right
        bad_node1.val, bad_node2.val = bad_node2.val, bad_node1.val
        print(bad_node2.val, bad_node1.val)


# method 1: change binary tree to a in-order list
# time O(n), space O(n)
# sort the values and then assign to the tree in order


class Solution1(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.inorder(root, nodes)
        if len(nodes) < 2:
            return
        vals = [node.val for node in nodes]
        vals.sort()
        for i, node in enumerate(nodes):
            node.val = vals[i]
            
    
    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)



"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def buildTreeLevelOrder(arr):
    if not arr or not arr[0]:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while i < len(arr):
        node = queue.popleft()
        if i < len(arr):
            if not arr[i]:
                left = None
            else:
                left = TreeNode(arr[i])
            node.left = left
            if left:
                queue.append(left)
            i += 1
        if i < len(arr):
            if not arr[i]:
                right = None
            else:
                right = TreeNode(arr[i])
            node.right = right
            if right:
                queue.append(right)
            i += 1
    return root

def printTree(root):
    res = []
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node:
                res.append(None)
            else:
                res.append(node.val)
            if node:
                queue.append(node.left)
                queue.append(node.right)
    print("print tree", res)
    
if __name__ == "__main__":
    root = buildTreeLevelOrder([1,3,None,None,2])
    printTree(root)
    
    Solution().recoverTree(root)
    
    