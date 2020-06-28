# time O(m^2*n^2), space O(m*n)
# brute force BFS, start from every building, and perform BFS for each of the BFS


from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        total_dists = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dists = self.bfs(grid, i, j)
                    self.addDists(grid, dists, total_dists)
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res = min(res, total_dists[i][j])
        return res if res != float('inf') else -1
    
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        visited[i][j] = True
        dists = [[float('inf')]*n for _ in range(m)]
        queue = deque([(i, j)])
        level = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                dists[x][y] = level
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + dx, y + dy
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 0 \
                    and not visited[p][q]:
                        visited[p][q] = True
                        queue.append((p, q))
            level += 1
        return dists
    
    def addDists(self, grid, dists, total_dists):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dists[i][j] == float('inf'):  # empty land (i, j) can not be reached by one house
                        grid[i][j] = 2    # mark it as a obstacle
                    else:
                        total_dists[i][j] += dists[i][j]


"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
