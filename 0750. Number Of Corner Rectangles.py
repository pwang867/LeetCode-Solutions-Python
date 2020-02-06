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
class Solution(object):
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


grid = [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]

print(Solution().countCornerRectangles(grid))
