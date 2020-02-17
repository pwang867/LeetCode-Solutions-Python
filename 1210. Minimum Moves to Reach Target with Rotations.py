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

"""
In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

 

Example 1:



Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9
 

Constraints:

2 <= n <= 100
0 <= grid[i][j] <= 1
It is guaranteed that the snake starts at empty cells.
"""
