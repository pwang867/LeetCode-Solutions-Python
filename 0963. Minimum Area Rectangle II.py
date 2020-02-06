# use (diagonal_length**2, center_point*2) as the key
# https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/208361/JAVA-O(n2)-using-Map     
from collections import defaultdict
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        d = defaultdict(list)
        for i in range(len(points)-1):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                key = self.gen_key(p1, p2)
                d[key].append([p1, p2])
        
        res = float('inf')
        for key, lines in d.items():
            if len(lines) < 2:
                continue
            for i in range(len(lines)-1):
                for j in range(i+1, len(lines)):
                    area = self.cal_area(lines[i], lines[j])
                    res = min(res, area)
        return res if res != float('inf') else 0  # mistake: res is not float('inf')
    
    def gen_key(self, p1, p2):
        """ use the length and center point as the key """
        length = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2  # avoid sqrt to keep numbers as int
        centerx = p1[0] + p2[0]  # avoid //2
        centery = p1[1] + p2[1]
        return (length, centerx, centery)
    
    def cal_area(self, line1, line2):
        """ line1 and line2 are the two diagonal lines of a rectangle, find its area"""
        p1, p2 = line1
        p3 = line2[0]
        edge1 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
        edge2 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
        return (edge1*edge2)**0.5


"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
"""
