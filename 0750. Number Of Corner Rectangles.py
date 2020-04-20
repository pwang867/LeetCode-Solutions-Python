# method 4, recommended by the hint in the problem
# time O(m*n^2), space O(n^2)
# when the matrix is very sparse, this method will be the best


class Solution4(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        cnt = 0
        _dict = collections.defaultdict(int)
        for r in range(len(grid)):
            for i in range(len(grid[0]) - 1):
                if grid[r][i] == 0:
                    continue
                for j in range(i + 1, len(grid[0])):
                    if grid[r][j] == 1:
                        cnt += _dict.get((i, j), 0)
                        _dict[(i, j)] += 1
        return cnt


# method 3, space O(1), but no optimized for sparse matrix

class Solution3(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        res = 0
        for i in range(len(grid) - 1):
            for j in range(i + 1, len(grid)):
                cnt = 0
                for k in range(len(grid[0])):
                    if grid[i][k] == grid[j][k] == 1:
                        cnt += 1
                res += cnt * (cnt - 1) // 2
        return res


# method 2, time O(m^2*n), space O(n)


class Solution2(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        res = 0
        for i in range(len(grid) - 1):
            set1 = {y for y in range(len(grid[0])) if grid[i][y] == 1}
            for j in range(i + 1, len(grid)):
                set2 = {y for y in range(len(grid[0])) if grid[j][y] == 1}
                cnt = len(set1.intersection(set2))
                res += cnt * (cnt - 1) // 2
        return res



# method 1, generalized method

"""
# this method make it a general case, such as matrix below
[
[7, 9, 6, 1, 7],
[8, 1, 0, 2, 1],
[7, 0, 1, 0, 7],
[1, 1, 6, 1, 1],
[5, 2, 9, 7, 1]
]
"""

# this problem is basically 2D dp problem, but it is dp[col][col]

from collections import defaultdict
class Solution1(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[defaultdict(int) for _ in range(n)] for i in range(n)]  
        # dp[i][j] = {vertice val: number of rows with row[i]==row[j]==val}
        res = defaultdict(int)  # {val: number of rectangles with vertice equal to val}
        for i in range(m):
            for p in range(n):
                for q in range(p+1, n):
                    if grid[i][p] == grid[i][q]:
                        num = grid[i][p]
                        dp[p][q][num] += 1
                        res[num] += dp[p][q][num]-1
        
        return res[1]


grid =  [[1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1]]

print(Solution4().countCornerRectangles(grid))



"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. 
Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.


Example 1:

Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:

Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:

Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.
"""