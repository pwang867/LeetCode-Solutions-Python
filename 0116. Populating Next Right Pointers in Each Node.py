# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


# method 2: iteration, space O(1)


class Solution2(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        row_head = root   # row_head is always the first node of one row/level
        while row_head and row_head.left:
            cur = row_head
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            row_head = row_head.left
        return root


# method 1: BFS, iteration, time O(n), space O(n)


class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        level = [root]
        
        while level:
            for i in range(len(level) - 1):  # connect nodes
                level[i].next = level[i + 1]
            level[-1].next = None
            
            level = [child for node in level \
                     for child in [node.left, node.right] if child]


"""
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer 
to point to its next right node, just like in Figure B.
"""
