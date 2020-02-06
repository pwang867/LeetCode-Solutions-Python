# this problem is basicly to find a route from (0,0) to (m-1, n-1) 
# that minimize the maximum elevation in the path

# method 2: Dijkstra, heap
import heapq
class Solution:
    def swimInWater(self, grid):
        if not grid or not grid[0]:
            return 0
        
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        while heap:
            elev, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            res = max(res, elev)
            if i==len(grid)-1 and j == len(grid[0])-1:
                return res
            for v in dirs:
                p, q = i + v[0], j + v[1]
                if 0 <= p < len(grid) and 0 <= q < len(grid[0]):
                    heapq.heappush(heap, (grid[p][q], p, q))
        

# method 1: union find, time/space O(m*n)
class Solution1:
    def swimInWater(self, grid):
        def union(a, b):  # a, b are two positions
            a = find(a)
            b = find(b)
            parent[a[0]][a[1]] = b
        
        def find(pos):
            if parent[pos[0]][pos[1]] == pos:
                return pos
            parent[pos[0]][pos[1]] = find(parent[pos[0]][pos[1]])  # flatten graph
            return parent[pos[0]][pos[1]]
        
        m = len(grid)
        n = len(grid[0])
        positions = {grid[i][j]: (i, j) for i in range(m) for j in range(n)}   # elevation: position
        parent = [[(i,j) for j in range(n)] for i in range(m)]
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for elev in range(m*n):  # elev is also time
            i, j = positions[elev]
            for v in dirs:
                p, q = i + v[0], j + v[1]
                if p >= 0 and p < m and q >= 0 and q < n and grid[p][q] <= elev:
                    union((i, j), (p, q))
                    if find((0, 0)) == find((m-1, n-1)):
                        return elev


"""
On an N x N grid, each square grid[i][j] represents the ground elevation 
at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere 
that has a ground elevation <= t is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""
