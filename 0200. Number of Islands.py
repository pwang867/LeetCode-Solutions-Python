# method 1: DFS, time O(n)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_island += 1
                    # mark all "1" to "2" for this island
                    self.markGrid(grid, i, j)  
        
        return num_island
    
    def markGrid(self, grid, i, j):
        grid[i][j] = "2"
        for v in [(1,0), (-1,0), (0,1), (0,-1)]:
            p, q = i + v[0], j + v[1]
            if p >= 0 and p < len(grid) and q >= 0 and q < len(grid[0]) \
            and grid[p][q] == "1":
                self.markGrid(grid, p, q)

        

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
