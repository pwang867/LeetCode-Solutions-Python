"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# iteration
class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        
        res = []
        
        stack = [root]
        pre = root
        while stack:
            p = stack[-1]
            if not p.children or pre in p.children:
                # process p
                stack.pop()
                res.append(p.val)
                pre = p
            else:
                for child in p.children[::-1]:
                    if child:
                        stack.append(child)
        
        return res


# recursion
class Solution1(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.postorderHelper(root, res)
        return res
    
    def postorderHelper(self, root, res):
        if not root:
            return
        
        for child in root.children:
            if child:
                self.postorderHelper(child, res)
        
        res.append(root.val)
        

"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:
    

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""
