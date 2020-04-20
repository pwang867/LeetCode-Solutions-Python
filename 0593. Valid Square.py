# edge case: 1. rectangle, 2. overlapping points
# time/space O(1)
# 1. center and length of two diagonals matches, 2. edges are the same


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        points.sort()
        p1, p2, p3, p4 = points   # reorder the four points
        return p1[0] + p4[0] == p2[0] + p3[0] and p1[1] + p4[1] == p2[1] + p3[1] \
               and self.dist(p1, p4) == self.dist(p2, p3) \
               and self.dist(p1, p2) == self.dist(p2, p4) and self.dist(p1, p2) != 0

    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""