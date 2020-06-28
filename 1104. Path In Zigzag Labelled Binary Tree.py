# search bottom up, use math, [2^h, 2^(h+1)-1]


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        h = 0
        high = 2
        while high - 1 < label:
            high *= 2
            h += 1
        res = []
        while label > 0:
            res.append(label)
            label = self.get_parent(label, h)
            h -= 1
        return res[::-1]

    def get_parent(self, label, h):
        if h % 2 == 0:
            return 2 ** h - 1 - (label - 2 ** h) // 2
        else:
            return 2 ** (h - 1) + (2 ** (h + 1) - 1 - label) // 2


"""
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, 
while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of 
the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
"""

