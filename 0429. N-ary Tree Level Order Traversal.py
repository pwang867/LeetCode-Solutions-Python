"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# standard BFS, time/space O(n)
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            vals = [node.val for node in queue]
            res.append(vals)
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    if child:
                        queue.append(child)
        return res


# recursion
class Solution1(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        self.levelOrderHelper(root, 0, res)
        return res
    
    def levelOrderHelper(self, root, level, res):
        if not root:
            return
        
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        
        for child in root.children:
            if child:
                self.levelOrderHelper(child, level+1, res)
        
"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""
