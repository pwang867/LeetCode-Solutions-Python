# method 1: time O(n)
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
        if grid[i][j] in ["0", "2"]:
            return
        
        grid[i][j] = "2"
        for v in [(1,0), (-1,0), (0,1), (0,-1)]:
            p, q = i + v[0], j + v[1]
            if p >= 0 and p < len(grid) and q >= 0 and q < len(grid[0]):
                self.markGrid(grid, p, q)
        
