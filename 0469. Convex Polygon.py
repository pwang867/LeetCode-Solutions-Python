# method 2, best solution, do not need to scan all points, time O(n), space O(1)
# use the rule that edge1 x edge2 should be the same direction
# this is basically to make sure all edges turns in the same direction, CW or CCW
class Solution2(object):
    def isConvex(self, points):
        if not points or len(points) < 3:
            return False
        n = len(points)
        direction = None
        for i in range(n):
            A, B, C = points[i], points[(i+1)%n], points[(i+2)%n]
            v1 = [A[0]-B[0], A[1]-B[1]]
            v2 = [C[0]-B[0], C[1]-B[1]]
            cross_product = v1[0] * v2[1] - v1[1] * v2[0]
            if cross_product == 0:
                continue
            elif direction == None:
                direction = 1 if cross_product > 0 else -1
            else:
                if direction*cross_product < 0:
                    return False
        return True

            
# method 1, use math equation, time O(n), space O(1)
# the sum of inner angles of a polygon should be (n-2)*pi
import numpy as np
class Solution1(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points or len(points) < 3:
            return False
        total = 0
        for i in range(1, len(points)-1):
            theta = self.cal_angle(points[i-1], points[i], points[i+1])
            if theta == 0:    #  edge case: theta == np.pi is allowed
                return False
            total += theta
        total += self.cal_angle(points[-1], points[0], points[1])
        total += self.cal_angle(points[-2], points[-1], points[0])
        return abs(total - (len(points)-2)*np.pi) < 1.0e-6
    
    def cal_angle(self, p1, p2, p3):
        v1 = [p1[0]-p2[0], p1[1]-p2[1]]
        v2 = [p3[0]-p2[0], p3[1]-p2[1]]
        v3 = [p3[0]-p1[0], p3[1]-p1[1]]
        v1_len = np.sqrt(v1[0]**2 + v1[1]**2)
        v2_len = np.sqrt(v2[0]**2 + v2[1]**2)
        v3_len = np.sqrt(v3[0]**2 + v3[1]**2)
        return np.arccos((v1_len**2 + v2_len**2 - v3_len**2)/2.0/v1_len/v2_len)
  

      
"""
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

 

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
 

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:
"""
