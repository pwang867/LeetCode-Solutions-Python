# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        print(root, key)
        print("\n")
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        # current root needs to be deleted
        if not root.left:  # when root only has one children
            return root.right
        if not root.right:
            return root.left
        
        # when root has two children
        if not root.left.right:
            new_root = root.left
            new_root.right = root.right
            root.right = None
            root.left = None
            return new_root
        else:
            # find the predecessor of root, and choose predecessor as the new root
            cur = root.left
            pre = cur.right
            while pre.right:
                cur = pre  # mistake: switch the position of this line the the line below
                pre = pre.right
            
            # pre will be the predecessor
            cur.right = pre.left
            pre.left = root.left
            pre.right = root.right
            root.right = None
            root.left = None
            return pre



"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


from collections import deque
def createTree(arr):
    root = TreeNode(arr[0])
    i = 1
    queue = deque([root])
    
    while i < len(arr):
        node = queue.popleft()
        if arr[i] is None:
            node.left = None
        else:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i >= len(arr):
            break
        if arr[i] is None:
            node.right = None
        else:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
        
    return root

def printTree(root):
    queue = deque([root])
    
    cnt = 18
    
    while queue and cnt:
        row = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                row.append(node.val)
            else:
                row.append(".")
                continue
            queue.append(node.left)
            queue.append(node.right)
        cnt -= 1
        row = map(str, row)
        padding = (35-len(row))//2*["-"]
        print(" ".join(padding + row + padding))


arr = [2,0,33,None,1,25,40,None,None,11,31,34,45,10,18,29,32,None,36,43,46,4,None,12,24,26,30,None,None,35,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None, None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6]
num = 33

root = createTree(arr)
printTree(root)

Solution().deleteNode(root, 33)
printTree(root)
