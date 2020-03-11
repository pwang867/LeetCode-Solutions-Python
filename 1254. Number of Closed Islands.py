# method 2, first label 0 to 1 starting from boundaries
# then count and label for the whole grid
# time O(m*n)

class Solution2(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        # mark edges
        for i in range(len(grid)):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][-1] == 0:
                self.dfs(grid, i, len(grid[0]) - 1)
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                self.dfs(grid, 0, j)
            if grid[-1][j] == 0:
                self.dfs(grid, len(grid) - 1, j)
        # count islands
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    num_island += 1
                    self.dfs(grid, i, j)
        return num_island

    def dfs(self, grid, i, j):
        grid[i][j] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(grid) and 0 <= q < len(grid[0]) \
            and grid[p][q] == 0:
                self.dfs(grid, p, q)


# method 1, use a label to record if we encountered a boundary
class Solution1(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.is_closed = True
                    self.dfs(grid, i, j)
                    if self.is_closed:
                        num_island += 1
        return num_island

    def dfs(self, grid, i, j):
        # flip all connected 0 (island) to 1
        # make self.is_closed as False if reaching boundary
        grid[i][j] = 1
        for v in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            p, q = i + v[0], j + v[1]
            if p < 0 or p >= len(grid) or q < 0 or q >= len(grid[0]):
                self.is_closed = False
                continue
            if grid[p][q] == 0:
                self.dfs(grid, p, q)


"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Accepted
"""