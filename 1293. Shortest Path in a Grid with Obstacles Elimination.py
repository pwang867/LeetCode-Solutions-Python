# BFS, time O(m*n*k), space O(m*n)
# visited[i][j] stores the smallest count of obstacles to reach (i, j)
from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[m*n+1]*n for _ in range(m)]   
        depth = 0
        queue = deque([(0, 0, grid[0][0])])
        while queue:
            for _ in range(len(queue)):
                i, j, cnt = queue.popleft()   # cnt is cnt of obstacles met
                if (i, j) == (m-1, n-1) and cnt <= k:
                    return depth
                if cnt > visited[i][j]:    
                    # a single BFS level might have many (i, j)
                    # only process for the one with smallest cnt
                    continue
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    p, q = i + dx, j + dy
                    if not (0 <= p < m and 0 <= q < n):
                        continue
                    new_cnt = cnt + grid[p][q]
                    if new_cnt < visited[p][q] and new_cnt <= k:
                        visited[p][q] = new_cnt
                        queue.append((p, q, new_cnt))
            depth += 1
        return -1


"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
Accepted
"""
