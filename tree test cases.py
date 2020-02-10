from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def printNode(self):
        print(self.val)
        if self.left:
            self.left.printNode()
        if self.right:
            self.right.printNode()

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


