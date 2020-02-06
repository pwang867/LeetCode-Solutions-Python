# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# level-order serialization
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        nodes = deque([])
        for x in data:
            if x == "#":
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(x)))
        if not nodes or nodes[0] == None:
            return None
        root = nodes.popleft()
        queue = deque([root])          # previous level, only contains non-None nodes
        while queue:
            parent = queue.popleft()
            left = nodes.popleft()
            right = nodes.popleft()
            parent.left = left
            parent.right = right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# use preorder traversal to serialize the tree
# use "#" to label the empty node
from collections import deque
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial_str = deque()
        self.serializeHelper(root, serial_str)
        return " ".join(serial_str)
    
    def serializeHelper(self, root, serial_str):
        if not root:
            serial_str.append("#")
            return
        
        serial_str.append(str(root.val))
        self.serializeHelper(root.left, serial_str)
        self.serializeHelper(root.right, serial_str)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split()
        data_list = deque(data_list)
        
        return self.deserializeHelper(data_list)
        
    def deserializeHelper(self, data_list):
        # data_list: collections.deque()
        if not data_list:
            return None
        val = data_list.popleft()
        if val == "#":
            return None
        
        root = TreeNode(int(val))
        root.left = self.deserializeHelper(data_list)
        root.right = self.deserializeHelper(data_list)
        return root
    
    
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
