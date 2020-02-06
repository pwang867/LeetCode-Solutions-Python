"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid or not grid[0]:
            return None
        return self.constructHelper(grid, 0, 0, len(grid)-1, len(grid[0])-1)
    
    def constructHelper(self, grid, i, j, p, q):
        # (i, j) is topleft, (p, q) is bottomright
        root = Node(grid[i][j], False, None, None, None, None)
        if i == p and j == q:
            root.isLeaf = True
            return root
        
        x, y = (i+p)//2, (j+q)//2
        root.topLeft     = self.constructHelper(grid, i,   j,   x, y)
        root.topRight    = self.constructHelper(grid, i,   y+1, x, q)
        root.bottomLeft  = self.constructHelper(grid, x+1, j,   p, y)
        root.bottomRight = self.constructHelper(grid, x+1, y+1, p, q)
        
        if root.topLeft.isLeaf and root.topRight.isLeaf and \
        root.bottomLeft.isLeaf and root.bottomRight.isLeaf and\
        root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val:
            root.isLeaf = True
            root.topLeft = None
            root.topRight = None
            root.bottomLeft = None
            root.bottomRight = None
        
        return root


"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:



 

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.



Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
"""
