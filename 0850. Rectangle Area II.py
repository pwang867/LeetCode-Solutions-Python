import bisect


class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        if not rectangles:
            return 0

        # find the appeared coordinates of rows and cols
        rows, cols = set(), set()
        for x1, y1, x2, y2 in rectangles:
            rows.add(x1)
            rows.add(x2)
            cols.add(y1)
            cols.add(y2)
        rows = sorted(list(rows))
        cols = sorted(list(cols))
        m, n = len(rows), len(cols)
        mark = [[False] * n for _ in range(m)]

        # mark sub rectangles
        for x1, y1, x2, y2 in rectangles:
            i1 = bisect.bisect_left(rows, x1)
            i2 = bisect.bisect_left(rows, x2)
            j1 = bisect.bisect_left(cols, y1)
            j2 = bisect.bisect_left(cols, y2)
            for i in range(i1, i2):
                for j in range(j1, j2):
                    mark[i][j] = True

        # find the total area
        area = 0
        N = 10 ** 9 + 7
        for i in range(m - 1):  # m*n points result in (m-1)*(n-1) rectangles
            for j in range(n - 1):
                if mark[i][j]:
                    area = (area + (rows[i + 1] - rows[i]) * (cols[j + 1] - cols[j])) % N
        return area


"""
We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] ,
where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates
of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large,
return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""