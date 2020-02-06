# time O(3^N), space O(N), N = len(grid)*len(grid[0])

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        start, n = self.init(grid)
        self.res = 0
        self.helper(grid, start[0], start[1], set(), n)
        return self.res
    
    def init(self, grid):
        start = (0, 0)
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    n += 1
        return (start, n)
    
    def helper(self, grid, i, j, path, n):
        if grid[i][j] == 2:
            if len(path) == n+1:
                self.res += 1
            return
        path.add((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(grid) and 0 <= q < len(grid[0]) \
            and (p, q) not in path and grid[p][q] != -1:
                self.helper(grid, p, q, path, n)
        path.remove((i, j))
        


"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
Accepted
"""
