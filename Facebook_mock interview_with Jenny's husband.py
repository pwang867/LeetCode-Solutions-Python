"""
Balanced binary tree


      1 (2)
    /   \
   3(1)   4(0)
  /
 5(0)


return True


      1
     / \
    3(2, invalid)   4
   /
  5(1)
 /
6(0)
False


None
True


validate

self.is_valid = False

depth(node): longest distance to leaf

O(n), O(depth)

"""


class Tree:

    def validate(self, node):
        return self.depth(node)

    def depth(self, node):  # node = 1
        # the depth from node to bottom leaf
        if not node:
            return 0
        left = self.depth(node.left)  # left = 0
        right = self.depth(node.right)
        res = max(left, right) + 1
        if abs(left[1] - right[1]) > 1 or left == -1 or right == -1:
            res = -1
        return res


