# union find
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        size   = {(i, j): 1      for i in range(m) for j in range(n) if grid[i][j] == 1}
        
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            return False
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx, dy in [(-1, 0), (0, -1)]:
                    p, q = i + dx, j + dy
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        union((i, j), (p, q))
        map(find, parent)
        
        # check the islands near current grid[i][j]==0
        res = 1
#        res = max(size.values())   # size might be empty and max will throw an error
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    res = max(res, size[find((i,j))])
                else:
                    roots = set()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        p, q = i + dx, j + dy
                        if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                            roots.add(find((p, q)))
                    # cur means the size of the max island if we change (i, j) from 0 to 1
                    cur = 1
                    for root in roots:
                        cur += size[root]
                    res = max(res, cur)
        
        return res




"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? 
(An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""
