# for combination problems, index don't have to look back
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) < 3:
            return len(points)
        
        res = 2
        for i in range(len(points)-1):
            d = defaultdict(int)
            duplicate = 1
            for j in range(i+1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                n = self.gcd(dx, dy)
                d[(dx//n, dy//n)] += 1
            cnt = max(d.values()) if d else 0
            res = max(res, cnt + duplicate)  # d could be empty
        return res
    
    def gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.gcd(y, x%y)



"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
"""
