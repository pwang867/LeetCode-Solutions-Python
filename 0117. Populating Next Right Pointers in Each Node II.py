# iteration, time O(n), space O(1)
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        copy = root
        
        while root:
            dummy = Node(0, None, None)
            cur = dummy
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = dummy.next
            dummy.next = None
        
        return copy


# BFS, time O(n), space O(n)
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
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
            