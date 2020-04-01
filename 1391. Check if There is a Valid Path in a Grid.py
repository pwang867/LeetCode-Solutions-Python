# method 2: BFS



# method 1, union find, time/space O(4*m*n), slow
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])
        parent = {(i, j): (i, j) for i in range(-1, 2*m) for j in range(-1, 2*n)}
        size = {(i, j): 0 for i in range(-1, 2*m) for j in range(-1, 2*n)}
        
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
                if grid[i][j] in [2, 5, 6]:  # connect center to top
                    union((2*i, 2*j), (2*i-1, 2*j))
                if grid[i][j] in [1, 3, 5]:  # connect center to left
                    union((2*i, 2*j), (2*i, 2*j-1))
                if grid[i][j] in [2, 3, 4]:  # bottom
                    union((2*i, 2*j), (2*i+1, 2*j))
                if grid[i][j] in [1, 4, 6]:  # right
                    union((2*i, 2*j), (2*i, 2*j+1))
        
        return find((0, 0)) == find((2*m-2, 2*n-2))


"""
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
