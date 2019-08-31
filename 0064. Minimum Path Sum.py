# method 2, dp
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        
        return grid[-1][-1]
    

# method 1, recursion with memo
class Solution1(object):
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        # memorization: {(i,j):minSum}
        self.memo = {(len(grid)-1, len(grid[0])-1): grid[-1][-1]}  
        return self.minPathSumRec(grid, 0, 0)
    
    def minPathSumRec(self, grid, i, j):
        # find the min sum of the path from (i, j) to the bottom right
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        right, bottom = float('inf'), float('inf')
        if j+1 < len(grid[0]):
            right = self.minPathSumRec(grid, i, j+1)
        if i+1 < len(grid):
            bottom = self.minPathSumRec(grid, i+1, j)
            
        self.memo[(i,j)] = grid[i][j] + min(right, bottom)
        return self.memo[(i,j)]
        

