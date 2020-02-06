# method 2, same preprocess as method 1, but the rectangle searching is more brute force
# no need to sort, by using set
# time O(n^2), space O(n)
from collections import defaultdict
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = defaultdict(set)
        for x, y in points:
            d[y].add(x)
        
        # p1 and p2 are the diagonal points, but the diagonal can be any one
        area = float('inf')
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if x2 in d[y1] and x1 in d[y2]:
                    area = min(area, abs((x2-x1)*(y2-y1)))
        return area if area != float('inf') else 0
    

# process the data to a dictionary of horizontal lines, 
# then scan line by line, save {(y1, y2):x} to another dictionary

# time O(n^2), space O(n)
from collections import defaultdict
class Solution1(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = defaultdict(list)
        for point in points:
            d[point[1]].append(point[0])    # mistake: d[point[1]].append(point)
        rows = d.keys()
        rows.sort()
        edges = defaultdict(int)   # horizontal edges, {(y1, y2): x}
        area = float('inf')
        for row in rows:
            vals = d[row]
            vals.sort()
            for i in range(len(vals)-1):
                for j in range(i+1, len(vals)):
                    edge = (vals[i], vals[j])
                    if edge in edges:
                        area = min(area, (vals[j]-vals[i])*(row - edges[edge]))
                    edges[edge] = row
        return area if area != float('inf') else 0  # mistake: return area if area == float('inf') else 0

"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

