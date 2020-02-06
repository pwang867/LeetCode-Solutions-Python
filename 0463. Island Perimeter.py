# method 3: recursively search starting from a single "1" point
# faster than method 2, because it does not have to check the whole grid
# however, it has large dfs depth
class Solution(object):
    def islandPerimeter(self, grid):
        peri = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.islandHelper(grid, i, j, peri)
                    break
        return peri[0]
    
    def islandHelper(self, grid, i, j, peri):
        # input requirement: grid[i][j] == 1
        grid[i][j] = 2
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for _dir in dirs:
            x, y = _dir[0] + i, _dir[1] + j
            if x < 0 or y < 0 or x >= len(grid) \
                or y >= len(grid[0]) or grid[x][y] == 0:
                peri[0] += 1
            elif grid[x][y] == 1:
                self.islandHelper(grid, x, y, peri)
                
        

# method 2: brute force, do not use padding
class Solution2(object):
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        
        peri = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
                        x, y = dir[0] + i, dir[1] + j
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                            peri += 1
        
        return peri


# method 1: brute force, use padding
class Solution1(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pad the edges of the grid with water
        grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]  
        new_grid = [[0] + row + [0] for row in grid]
        
        perimeter = 0
        
        for i in range(1, len(new_grid)-1):
            for j in range(1, len(new_grid[0])-1):
                if new_grid[i][j] == 1:
                    perimeter += 4 - new_grid[i-1][j] - new_grid[i+1][j] \
                                    - new_grid[i][j-1] - new_grid[i][j+1]
        
        return perimeter
    
        
