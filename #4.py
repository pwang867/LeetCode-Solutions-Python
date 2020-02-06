from collections import deque
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid[0]) < 2:
            return 0
        
        n = len(grid)
        target = (n-1, n-2, n-1, n-1)
        
        depth = 0
        queue = deque([(0, 0, 0, 1)])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                pos = queue.popleft()
                if pos in visited:
                    continue
                visited.add(pos)
                
                if pos == target:
                    return depth
                
                neighbors = self.getNextPositions(grid, pos)
                queue.extend(neighbors)
                
            depth += 1
        
        return -1
    
    def getNextPositions(self, grid, pos):
        res = []
        r1, c1, r2, c2 = pos
        if r2+1 < len(grid) and grid[r1+1][c1] == 0 and grid[r2+1][c2] == 0:  # move down
            res.append((r1+1, c1, r2+1, c2))
        if c2+1 < len(grid[0]) and grid[r1][c1+1]==0 and grid[r2][c2+1] == 0:     # move right
            res.append((r1, c1+1, r2, c2+1))
        if r1 == r2 and r1+1 < len(grid) and grid[r1+1][c1] == 0 and grid[r2+1][c2] == 0:  # rotate down
            res.append((r1, c1, r1+1, c1))
        if c1 == c2 and c1+1 < len(grid[0]) and grid[r1][c1+1] == 0 and grid[r2][c2+1] == 0:  # rotate up
            res.append((r1, c1, r1, c1+1))
        return res
    

grid = [[0,0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,1,0,1],[1,0,0,1,0,0,1,0,1,0],[0,0,0,1,0,1,0,1,0,0],[0,0,0,0,1,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0]]

print(len(grid))
print(Solution().minimumMoves(grid))
