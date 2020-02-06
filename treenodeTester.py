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

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root = node1
root.left = node2
root.right = node3
#root.printNode()
node1.printNode()

